import markdown

markdown_text = """
## Executive Summary for the School Board and Mayor's Office

---

### 1. Difference in Performances Between School Types
Our analysis of over 39,170 students across district-wide standardized tests indicates that **charter schools significantly outperform district schools** in both math and reading. Notably, even the lowest-performing charter school surpasses the highest-performing district school by approximately 35% in overall passing rates. This vast contrast suggests that the strategies utilized by charter schools—such as fewer student numbers and personalized teaching methods—are more effective in achieving higher success.

### 2. School Size and Funding
The data shows a counterintuitive trend: schools with **lower spending per student tend to achieve better results**. Also, smaller schools consistently report higher passing rates, pointing to the challenges larger institutions face in maintaining quality. These observations are critical for district schools, which often have larger student counts and higher per-student spending but do not correspondingly reflect higher numbers.

### 3. Strategic Recommendations
- **Resource Reallocation:** Funds should be directed towards direct educational avenues, such as improving teacher quality and student services, rather than administrative overheads or extracurriculars that provide additional distractions.
- **Adopting Best Practices:** District schools may benefit from adopting charter school strategies, including reducing student-to-teacher ratios and enhancing more personable instruction.
- **Further Research:** A deeper dive into the expenditure and its direct correlation with student outcomes is necessary to optimize budget allocations.

---

### Conclusion
The data-driven insights presented call for a strategic overhaul of budget allocations and educational practices, particularly in district schools. By implementing proven successful models from charter schools, the board can enhance overall student performance and education quality.
"""

css_style = """
<style>
body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; color: DimGrey; }
h2 { color: Teal; }
h1, h3 { color: DarkMagenta; }
</style>
"""
html_content = markdown.markdown(markdown_text)
html_output = css_style + html_content

with open('styled_report.html', 'w', encoding='utf-8') as f:
    f.write(html_output)
    
print("HTML report created successfully.")



