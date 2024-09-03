# Oliver - Your Judgmental UI Design AI 🧔👓
![Oliver](assets/oliver_ui_hero.png)

## Meet Oliver: The Hipster AI Who'll Roast Your UI 🔥

Ever wished for a brutally honest, slightly condescending, but undeniably brilliant UI designer to critique your website? Say hello to **Oliver** - the Python package that brings the discerning eye of a Brooklyn hipster UI designer right to your codebase.

### What's Oliver's Deal? 🤔

Oliver isn't just another run-of-the-mill design critic. He's a sophisticated AI powered by the latest in machine learning, with a dash of artisanal, small-batch sarcasm. Here's what he brings to your digital table:

- **Pixel-Perfect Precision**: Oliver scrutinizes every element of your UI with the intensity of someone choosing the perfect pour-over coffee beans.
- **Trendsetter Perspective**: Get feedback that's so cutting-edge, it's practically bleeding (but in a cool, indie band album cover kind of way).
- **Actionable Insights**: Because even Oliver knows that criticism without solutions is like a fixie without a custom paint job - pointless.
- **Structured Output**: Oliver doesn't just rant; he provides structured JSON that's ready for the next step in your design evolution.

## Why Oliver? Because Your UI Deserves Better 💅

Let's face it, your website could use a makeover. And who better to guide you than an AI with an attitude and a man bun? Oliver offers:

- **Detailed Reports**: Long-form critiques that dive deep into your design choices, questioning every pixel like it owes him money.
- **Real-Time Feedback**: Integrate Oliver into your workflow and get instant critiques. It's like pair programming, but with more sighs and eye-rolls.
- **Cross-Platform Analysis**: Oliver judges your desktop and mobile designs equally, because discriminating against screen sizes is so last season.
- **Structured Suggestions**: Get your critique in JSON format, perfect for feeding into other tools or your own custom workflows.

## How to Unleash Oliver on Your Unsuspecting UI 🚀

1. **Install the package**: `pip install oliver` (warning: may cause sudden urges to brew kombucha)
2. **Point Oliver at your site**:
   ```python
   from oliver import WebpageCritique

   url = "https://your-soon-to-be-roasted-website.com"
   description = "An attempt at design that Oliver will surely have opinions about"
   
   critic = WebpageCritique(llm_model='gpt-4o')
   roast = critic.critique_webpage(url, description)
   
   print(json.dumps(roast, indent=2))  # Brace yourself for Oliver's thoughts
   ```

## What You'll Get 📊

Oliver doesn't just throw around pretentious jargon (well, maybe a little). He provides structured, insightful feedback on your UI:

- **Visual Hierarchy**: "Your call-to-action button is about as noticeable as a vegan at a steakhouse."
- **Color Scheme**: "This palette is more clashing than a noise rock concert. Let's tone it down, shall we?"
- **Typography**: "Your font choices are giving me 'ransom note' vibes. Time for an intervention."
- **Layout**: "This layout is more confusing than a mainstream film plot. Let's streamline."

And the best part? All of this comes in a neatly structured JSON format, ready for your next move.

## Why It's Actually Useful 💡

Beyond the snark and the laughs, Oliver is a powerful tool for developers and designers:

- **Instant Feedback**: Catch UI issues early, before they become embarrassing launch-day features.
- **Consistency Checks**: Oliver ensures your design language is more coherent than a single-origin espresso.
- **Improved UX**: Turn Oliver's sass into genuinely better user experiences.
- **Integration-Ready Output**: Oliver's structured feedback is perfect for plugging into your existing tools and workflows.

## The Tech Behind the Turtleneck 🧠

Oliver isn't just a pretty face with great taste. He's powered by:

- **Selenium**: For capturing those high-res screenshots Oliver loves to judge.
- **GPT-4**: Providing the brains behind the sarcasm.
- **Computer Vision**: Because Oliver needs to see your design crimes to critique them properly.

## Coming Soon: Oliver's Code Makeover 🚧

Exciting news! Soon, Oliver won't just tell you what's wrong with your UI - he'll fix it for you. That's right, we're working on a feature that will take Oliver's structured output and use it to generate code snippets for implementing his suggestions. 

Imagine: You run Oliver on your site, he gives you his usual snarky feedback, but then he also hands you the CSS and HTML tweaks to make it right. It's like having a hipster UI designer and a coding wizard in one package (man bun included, coding skills optional).

Stay tuned for this game-changing feature. Your UI is about to get a makeover, Oliver style.

## In Conclusion

Whether you're a seasoned designer looking for a fresh perspective or a developer who thinks Comic Sans is "misunderstood," Oliver is here to set you straight. Get ready for brutally honest, hilariously snarky, and surprisingly insightful UI critiques that'll whip your designs into shape faster than you can say "artisanal cold brew."

So go ahead, give Oliver a try. Your users will thank you (and Oliver will make sure you know it was all his idea).

---

Remember, in the world of UI design, it's Oliver's way or the highway. And the highway probably has better kerning.