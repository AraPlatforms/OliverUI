# Oliver - Your Helpful UI Design AI

![Oliver](assets/oliver_ui_hero.png)

## Introducing Oliver: The AI That Will Enhance Your UI Design

**Oliver** is a Python package designed to provide thorough and insightful critiques of your website's UI. With the latest in machine learning, Oliver brings a level of precision and analysis that can help you improve your design efficiently.

### What Does Oliver Do?

Oliver is more than just a design critic; he is an AI that provides valuable feedback to help you refine your UI. Here’s what Oliver offers:

- **Pixel-Perfect Analysis**: Oliver examines every detail of your UI to ensure it meets high design standards.
- **Trend-Aware Feedback**: Oliver’s suggestions are based on current design trends, ensuring your site stays modern and appealing.
- **Actionable Insights**: Oliver provides not just critiques but also practical suggestions to enhance your design.
- **Structured Output**: Oliver delivers his feedback in a well-organized JSON format, making it easy to implement improvements.

## Why Use Oliver?

If your website needs a design review, Oliver is here to help. Here’s what you can expect:

- **Detailed Reports**: In-depth critiques of your design choices with suggestions for improvement.
- **Real-Time Feedback**: Integrate Oliver into your workflow to receive instant design critiques.
- **Cross-Platform Analysis**: Oliver evaluates both desktop and mobile versions of your site.
- **Structured Suggestions**: Receive Oliver’s feedback in JSON format, perfect for integrating with other tools or workflows.

## How to Get Started with Oliver

1. **Install the package**: `pip install oliver`
2. **Point Oliver at your site**:
   ```python
   from oliver import WebpageCritique

   url = "https://your-website.com"
   description = "A design critique from Oliver"
   
   critic = WebpageCritique(llm_model='gpt-4o')
   critique = critic.critique_webpage(url, description)
   
   print(json.dumps(critique, indent=2))
   ```

## What Oliver Provides

Oliver’s feedback is structured and focused on improving your UI:

- **Visual Hierarchy**: Suggestions on how to make important elements stand out.
- **Color Scheme**: Recommendations for a cohesive and visually appealing color palette.
- **Typography**: Advice on font choices to enhance readability and aesthetic appeal.
- **Layout**: Tips on organizing your layout for better user experience.

All feedback is provided in a structured JSON format, ready for implementation.

## Why Oliver is Valuable

Oliver is a powerful tool for developers and designers looking to improve their UI:

- **Instant Feedback**: Identify and address UI issues early in the design process.
- **Consistency Checks**: Ensure your design language is consistent across all elements.
- **Improved UX**: Use Oliver’s feedback to create better user experiences.
- **Integration-Ready Output**: Oliver’s feedback is easily integrated into your existing workflows.

## The Technology Behind Oliver

Oliver is powered by:

- **Selenium**: Captures high-resolution screenshots for analysis.
- **GPT-4**: Provides the intelligence behind Oliver’s feedback.
- **Computer Vision**: Enables Oliver to accurately assess your design.

## Upcoming Features: Code Generation

We’re working on a new feature where Oliver will not only critique your UI but also generate code snippets to implement his suggestions. This will make it even easier to enhance your design based on Oliver’s feedback.

## Conclusion

Oliver is here to help you create better UIs. Whether you’re a seasoned designer or a developer, Oliver provides valuable insights that can significantly improve your website’s design.

Try Oliver today and see the difference in your UI.