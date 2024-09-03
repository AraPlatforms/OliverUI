from selenium import webdriver
from io import BytesIO
from pathlib import Path
from PIL import Image
import base64
import re

from llm_helpers import *
from prompts import Prompts

class WebpageCritique:
    def __init__(self, llm_model='gpt-4o-mini'):
        self.llm_model = llm_model

    def capture_screenshots(self, url):
        desktop_size = (1920, 1080)
        mobile_size = (375, 812)  # iPhone X size

        screenshots = {
            'desktop': self._capture_viewport_screenshots(url, desktop_size),
            'mobile': self._capture_viewport_screenshots(url, mobile_size)
        }
        
        return screenshots

    def _capture_viewport_screenshots(self, url, viewport_size):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f"--window-size={viewport_size[0]},{viewport_size[1]}")
        
        driver = webdriver.Chrome(options=options)
        
        try:
            driver.get(url)
            
            # Get the total height of the page
            total_height = driver.execute_script("return document.body.scrollHeight")
            
            # Set the window height
            window_height = viewport_size[1]
            
            screenshots = []
            offset = 0
            
            while offset < total_height:
                # Scroll to the current position
                driver.execute_script(f"window.scrollTo(0, {offset});")
                
                # Capture screenshot
                screenshot = driver.get_screenshot_as_png()
                img = Image.open(BytesIO(screenshot))
                
                # Convert to base64
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                screenshots.append(f"data:image/png;base64,{img_str}")
                
                # Move to the next section
                offset += window_height
        
        finally:
            driver.quit()
        
        return screenshots

    def critique_webpage(self, url, description):
        screenshots = self.capture_screenshots(url)
        
        prompt = Prompts.ui_critique_inputs.format(description=description)
        
        # Combine desktop and mobile screenshots
        all_screenshots = screenshots['desktop'] + screenshots['mobile']
        
        response = llm_call(
            prompt=prompt,
            context=[Prompts.ui_critique_instructions],
            model_name=self.llm_model,
            img_urls=all_screenshots,
            force_json=True
        )
        
        return json.loads(response)
    
    def _extract_code_from_backticks(self, text):
        pattern = r'```(?:\w+)?\s*([\s\S]*?)```'
        matches = re.findall(pattern, text, re.MULTILINE)
        
        if not matches:
            return text.strip()
  
        longest_block = max(matches, key=len)        
        code = re.sub(r'^(?:\w+\s*\n|<\w+>\s*\n)', '', longest_block, flags=re.MULTILINE)
        
        return code.strip()
    
    def generate_markdown_report(self, critique):
        # Use the provided prompts and LLM to generate a markdown report
        prompt = Prompts.report_generation_inputs.format(
            critique=str(critique)
        )
        
        report = llm_call(
            prompt=prompt,
            context=[Prompts.report_generation_instructions],
            model_name=self.llm_model,
            max_tokens=4096,
            force_json=False
        )
        
        return self._extract_code_from_backticks(report)
    

if __name__ == '__main__':
    
    url = "https://www.ara.social"
    description = 'The landing page for an early stage startup. Optimizing for people reaching out.'
    
    critic = WebpageCritique(llm_model='gpt-4o')
    
    critique = critic.critique_webpage(url, description)    
    print(json.dumps(critique, indent=2))
    
    report = critic.generate_markdown_report(critique)

    print(report)
