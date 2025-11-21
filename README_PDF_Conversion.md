# How to Convert Documentation to PDF

## Quick Start

### Option 1: Using Python Script (Automatic)

```bash
# Install dependencies
pip install weasyprint markdown2

# Run conversion
python generate_pdf_documentation.py
```

This will generate `TARNET_Project_Documentation.pdf` in the same directory.

### Option 2: Using Pandoc (Best Quality)

```bash
# Install pandoc (if not installed)
# macOS: brew install pandoc basictex
# Linux: sudo apt-get install pandoc texlive-xetex
# Windows: Download from https://pandoc.org/installing.html

# Convert to PDF
pandoc TARNET_Project_Documentation.md -o TARNET_Project_Documentation.pdf \
  --pdf-engine=xelatex \
  --toc \
  --variable=mainfont:Georgia \
  --variable=fontsize:11pt \
  --variable=geometry:margin=2cm \
  --highlight-style=tango
```

### Option 3: Using Online Converter

1. Go to https://www.markdowntopdf.com/
2. Upload `TARNET_Project_Documentation.md`
3. Download the generated PDF

### Option 4: Using VS Code Extension

1. Install the "Markdown PDF" extension in VS Code
2. Open `TARNET_Project_Documentation.md`
3. Right-click → "Markdown PDF: Export (pdf)"

## Documentation Contents

The PDF includes:

1. **Executive Summary** - Key findings at a glance
2. **Introduction** - From SVAR to Causal ML
3. **Theoretical Background** - Causal inference fundamentals
4. **Research Design** - Treatment, outcome, controls
5. **Data and Methodology** - Preprocessing pipeline
6. **Model Architecture** - TARNet structure
7. **Results and Interpretation** - ATE, ITE, CATE explanation
8. **Key Findings** - Policy effectiveness insights
9. **Practical Applications** - For policymakers and researchers
10. **Code Structure** - Implementation overview
11. **Conclusion** - Summary and future directions
12. **Appendix** - How to use with real data

## Features

- ✅ **Comprehensive**: Covers theory, methodology, and results
- ✅ **Interpretable**: Clear explanations of all metrics
- ✅ **Printable**: Formatted for A4 paper
- ✅ **Professional**: Academic-style presentation
- ✅ **Practical**: Includes code examples and usage instructions

