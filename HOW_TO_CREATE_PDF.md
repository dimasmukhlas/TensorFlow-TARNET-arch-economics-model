# How to Create PDF Documentation

## Quick Guide

This guide explains how to convert the TARNET project documentation into a printable PDF format.

## Files Created

1. **TARNET_Project_Documentation.md** - Complete project documentation (theory, methodology, interpretation)
2. **Results_Interpretation_Report.md** - Auto-generated from model results (run Cell 25 after training)
3. **generate_pdf_documentation.py** - Python script for PDF conversion

---

## Method 1: Using Python Script (Recommended for Mac/Linux)

### Step 1: Install Dependencies

```bash
# Activate your environment
source tft_env/bin/activate

# Install required packages
pip install weasyprint markdown2
```

### Step 2: Run Conversion Script

```bash
python generate_pdf_documentation.py
```

This will create `TARNET_Project_Documentation.pdf` in the current directory.

---

## Method 2: Using Pandoc (Best Quality)

### Step 1: Install Pandoc

**macOS:**
```bash
brew install pandoc basictex
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended
```

**Windows:**
Download from: https://pandoc.org/installing.html

### Step 2: Convert to PDF

```bash
pandoc TARNET_Project_Documentation.md -o TARNET_Project_Documentation.pdf \
  --pdf-engine=xelatex \
  --toc \
  --variable=mainfont:Georgia \
  --variable=fontsize:11pt \
  --variable=geometry:margin=2cm \
  --highlight-style=tango
```

---

## Method 3: Using Online Converter (Easiest)

1. Go to: https://www.markdowntopdf.com/
2. Upload `TARNET_Project_Documentation.md`
3. Click "Convert to PDF"
4. Download the generated PDF

**Alternative sites:**
- https://dillinger.io/ (export to PDF)
- https://stackedit.io/ (export to PDF)

---

## Method 4: Using VS Code Extension

1. Install VS Code extension: "Markdown PDF" (yzane)
2. Open `TARNET_Project_Documentation.md` in VS Code
3. Right-click in the editor
4. Select "Markdown PDF: Export (pdf)"

---

## Method 5: Using Jupyter Notebook

If you're already in the notebook:

1. Install: `pip install nbconvert`
2. Export notebook: `jupyter nbconvert --to pdf [2]TARNET-example.ipynb`
3. Note: This exports the entire notebook, not just the documentation

---

## What's Included in the PDF

The PDF documentation contains:

### 1. Executive Summary
- Key findings at a glance
- Main conclusions

### 2. Introduction
- From SVAR to Causal ML
- Research motivation
- Problem statement

### 3. Theoretical Background
- Causal inference fundamentals
- ATE, ITE, CATE definitions
- TARNet architecture explanation

### 4. Research Design
- Treatment variable (LTV tightening)
- Outcome variable (housing price change)
- Control variables

### 5. Data and Methodology
- Data generation
- Preprocessing pipeline
- Train/test splits

### 6. Model Architecture
- Network structure diagram
- Training strategy
- Regularization

### 7. Results and Interpretation ⭐
**Detailed interpretation of:**
- **ATE:** What does the average effect mean?
- **ITE:** How do effects vary across units?
- **CATE:** How do effects differ by subgroups?
- **Counterfactuals:** What would have happened?

### 8. Key Findings
- Policy effectiveness
- Heterogeneity insights
- Nonlinear patterns

### 9. Practical Applications
- For policymakers
- For researchers
- For practitioners

### 10. Code Structure
- Implementation overview
- Data flow diagram

### 11. Conclusion
- Summary
- Future directions

### 12. Appendix
- How to use with real data
- Code examples
- Glossary

---

## Interpretation Guide

### Understanding ATE

**Example: ATE = -0.489**

**Interpretation:**
- **Sign:** Negative = Policy reduces price growth
- **Magnitude:** 0.489 percentage points = Moderate effect
- **Policy Implication:** LTV tightening effectively cools housing markets

**How to Read:**
- If ATE < 0: Policy reduces housing price growth
- If ATE > 0: Policy increases housing price growth
- Larger absolute value = Stronger effect

### Understanding ITE Distribution

**Key Statistics:**
- **Mean ITE:** Should be close to ATE
- **Standard Deviation:** Measures heterogeneity
  - High std (>0.5) = High variation in effects
  - Low std (<0.3) = Uniform effects
- **Range (min to max):** Shows how much effects vary

**Interpretation:**
- Most negative ITEs = Policy works for most units
- Large range = Context-dependent effectiveness

### Understanding CATE

**Example:**
```
High Credit Gap: CATE = -0.65
Low Credit Gap:  CATE = -0.32
```

**Interpretation:**
- Policy is **2x more effective** in high credit gap regions
- **Policy Recommendation:** Target high credit gap regions first

**How to Compare:**
- Compare CATE values across subgroups
- Larger absolute CATE = Stronger effect for that subgroup
- Differences indicate where to apply policy

### Understanding Counterfactuals

**For Treated Units:**
- **Observed:** What actually happened (with treatment)
- **Counterfactual:** What would have happened (without treatment)
- **Difference:** Treatment effect

**For Control Units:**
- **Observed:** What actually happened (without treatment)
- **Counterfactual:** What would happen (with treatment)
- **Difference:** Predicted treatment effect

**Interpretation:**
- Large differences = Strong policy impact
- Similar counterfactuals = Weak policy impact

---

## Tips for PDF Generation

1. **Check formatting:** Review the markdown file first
2. **Adjust margins:** Use geometry settings for more/less margin
3. **Font size:** Adjust fontsize variable (10pt, 11pt, 12pt)
4. **Page breaks:** The document is formatted to avoid awkward breaks
5. **Tables:** May need adjustment if very wide

---

## Troubleshooting

### Issue: PDF generation fails

**Solution:**
- Try Method 3 (online converter) - most reliable
- Check markdown syntax is correct
- Ensure file encoding is UTF-8

### Issue: Formatting looks wrong

**Solution:**
- Use Pandoc (Method 2) for best control
- Adjust CSS/styling in Python script
- Check markdown syntax

### Issue: Missing fonts

**Solution:**
- Pandoc: Install additional fonts or change mainfont
- WeasyPrint: Uses system fonts, may vary by OS

---

## Next Steps

1. ✅ Generate `TARNET_Project_Documentation.pdf`
2. ✅ Run Cell 25 in notebook to generate `Results_Interpretation_Report.md`
3. ✅ Convert interpretation report to PDF (same methods)
4. ✅ Combine both PDFs if needed

---

## Support

For questions:
- Check the markdown files for syntax issues
- Review generated HTML (intermediate step) if using weasyprint
- Consult Pandoc documentation: https://pandoc.org/MANUAL.html

