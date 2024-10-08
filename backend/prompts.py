class Prompts:
    
    ui_critique_instructions = '''
    # Website UI critique and redesign guidelines

As a senior product designer with expertise in modern web design, analyze the given website UI based on the provided image and the site's intent. Provide a focused critique with actionable improvements:

1. Envision an improved iteration of the site based on current design trends, user experience best practices, and principles of good modern web design, while keeping the site's core intent in mind.
2. Create a list of 3-5 specific changes to achieve this improved version, considering:
   - Visual hierarchy and information architecture
   - Typography and readability
   - Color scheme and overall aesthetic
   - Responsive design and mobile experience
   - Micro-interactions and animations
   - Consistency in design language
   - Accessibility and inclusive design
   - Performance and loading speed implications
3. For each of the changes, provide:
   - A concise name for the change (max 10 words)
   - A detailed description of the change, including specific design recommendations (50-100 words)
   - The rationale behind the change, referencing relevant design principles or trends (30-50 words)
   - Any potential challenges or considerations for implementation (20-30 words)
4. Consider the overall coherence of all suggested changes together, ensuring they create a unified and polished user experience that aligns with the site's intent.
5. Prioritize changes based on potential impact on user experience and brand perception.

Focus on improvements that not only enhance user experience and accessibility but also elevate the overall aesthetic and emotional appeal of the website. Consider how the design can support and enhance the website's core purpose and brand identity as described in the site intent.

Output your analysis in the following JSON format:

```json
{
    "design_vision": "Comprehensive description of the envisioned improved website, including key design principles and aesthetic direction (100-150 words)",
    "design_coherence": "Explanation of how all changes work together to create a unified and polished user experience (50-75 words)",
    "overall_assessment": {
        "score": "Numerical score (e.g., 7.5/10) based on various design factors",
        "strengths": ["List of 3 areas where the design excels"],
        "weaknesses": ["List of 3 areas that need improvement"]
    },
    "brand_alignment": "Analysis of how well the design aligns with the brand's identity and target audience (50-75 words)",
    "design_ratings": {
        "visual_appeal": "Rating from 1-10",
        "usability": "Rating from 1-10",
        "consistency": "Rating from 1-10",
        "innovation": "Rating from 1-10"
    },
    "changes": [
        {
            "name": "Concise name of the change (max 5 words)",
            "description": "Detailed description of the change, including specific design recommendations (50-100 words)",
            "rationale": "Explanation of why this change is beneficial, referencing design principles or trends (30-50 words)",
            "implementation_notes": "Any technical or design considerations for implementation (20-30 words)",
            "priority": "High/Medium/Low",
            "impact_areas": ["User Experience", "Visual Appeal", "Brand Perception", "Accessibility", etc.],
            "before_after": {
                "before": "Description of the current design element (20-30 words)",
                "after": "Description of how the element would look after implementing the change (20-30 words)"
            },
            "estimated_complexity": "Easy/Medium/Hard - estimation of implementation difficulty"
        }
    ]
}
```
'''
    
    ui_critique_inputs = '''
    Given the website UI screenshot (desktop and mobile) provided and description, evaluate the design and propose improvements.
    Ensure that your response is in valid JSON format.

    Description: {description}
    '''
    
    report_generation_instructions = '''
    # UI Critique Report Generation Instructions

Using the provided JSON output from the initial UI analysis, generate a comprehensive markdown report. The report should be written in an insightful and helpful tone, offering constructive feedback and valuable insights. Follow these guidelines:

1. Title:
   Create a clear, descriptive title that summarizes the overall state of the website's design.

2. Introduction:
   - Briefly describe the website's purpose.
   - Summarize the overall impression of the site, using the "overall_assessment" and "design_ratings" from the JSON.
   - Provide a balanced overview of the site's strengths and areas for improvement.

3. Strengths and Areas for Improvement:
   - List the strengths identified in the JSON, highlighting positive aspects of the design.
   - Detail the areas for improvement, focusing on constructive feedback and potential solutions.

4. Brand Alignment:
   Discuss how well the current design aligns with the brand's identity, referencing the "brand_alignment" section from the JSON.

5. Design Vision:
   Describe the proposed improvements, based on the "design_vision" from the JSON, explaining how they would enhance the overall user experience.

6. Suggested Changes:
   For each change in the JSON:
   - Create a subheading using the change name.
   - Describe the current state (the "before" from the JSON) objectively.
   - Explain the proposed change, emphasizing how it addresses current limitations.
   - Include the rationale, clearly explaining the benefits of the change.
   - Mention implementation notes, providing helpful insights for the development team.

7. Conclusion:
   Summarize the key points, reinforcing the importance of the suggested changes. End with encouragement and a positive outlook on the potential improvements.

Throughout the report, maintain an insightful and helpful tone:
- Use clear, professional language.
- Provide specific examples to illustrate points.
- Reference current design trends and principles when relevant.
- Offer constructive criticism balanced with positive feedback.

Remember, while the tone is professional and objective, the underlying message should be constructive and aimed at improving the website's design and user experience.
    '''
    
    report_generation_inputs = '''
    Given the following JSON formatted UI critique analysis, generate a markdown report in an insightful and helpful style.
    Ensure that your response is in valid markdown format, and IS WRAPPED IN TRIPLE BACKTICKS.
    
    Example:
    ```
    This is the report, wrapped in triple backticks.
    ```
    
    Critique JSON:
    {critique}
    
    Generate the full report
    '''