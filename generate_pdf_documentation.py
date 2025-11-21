#!/usr/bin/env python3
"""
Convert TARNET Project Documentation to PDF
Requires: markdown2, weasyprint (or pandoc)
"""

import os
import sys

def check_dependencies():
    """Check if required packages are installed"""
    missing = []
    
    try:
        import markdown2
    except ImportError:
        missing.append("markdown2")
    
    try:
        import weasyprint
    except ImportError:
        # Try pandoc instead
        try:
            import pypandoc
        except ImportError:
            missing.append("weasyprint or pypandoc")
    
    if missing:
        print("="*70)
        print("MISSING DEPENDENCIES")
        print("="*70)
        print("\nPlease install required packages:")
        print(f"\npip install {' '.join(missing)}")
        if "weasyprint" in str(missing):
            print("\nFor weasyprint:")
            print("  pip install weasyprint")
            print("\nFor pandoc (alternative):")
            print("  pip install pypandoc")
            print("  # Also install pandoc binary: https://pandoc.org/installing.html")
        print("\n" + "="*70)
        return False
    return True

def convert_with_weasyprint(md_file, pdf_file):
    """Convert markdown to PDF using weasyprint"""
    try:
        import markdown2
        from weasyprint import HTML, CSS
        
        # Read markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(
            md_content,
            extras=['fenced-code-blocks', 'tables', 'header-ids']
        )
        
        # Add CSS styling
        html_with_style = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            page-break-after: avoid;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 5px;
            margin-top: 30px;
            page-break-after: avoid;
        }}
        h3 {{
            color: #7f8c8d;
            margin-top: 25px;
            page-break-after: avoid;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            page-break-inside: avoid;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #ecf0f1;
            font-style: italic;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        .page-break {{
            page-break-before: always;
        }}
        .no-break {{
            page-break-inside: avoid;
        }}
        strong {{
            color: #2c3e50;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .toc {{
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
        """
        
        # Convert HTML to PDF
        HTML(string=html_with_style).write_pdf(pdf_file)
        print(f"✅ PDF generated successfully: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting with weasyprint: {e}")
        return False

def convert_with_pandoc(md_file, pdf_file):
    """Convert markdown to PDF using pandoc"""
    try:
        import pypandoc
        
        pypandoc.convert_file(
            md_file,
            'pdf',
            outputfile=pdf_file,
            extra_args=[
                '--pdf-engine=xelatex',
                '--variable=mainfont:Georgia',
                '--variable=fontsize:11pt',
                '--variable=geometry:margin=2cm',
                '--toc',
                '--highlight-style=tango'
            ]
        )
        print(f"✅ PDF generated successfully: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting with pandoc: {e}")
        return False

def main():
    """Main conversion function"""
    print("="*70)
    print("TARNET PROJECT DOCUMENTATION → PDF CONVERTER")
    print("="*70)
    
    # File paths
    md_file = "TARNET_Project_Documentation.md"
    pdf_file = "TARNET_Project_Documentation.pdf"
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"❌ Error: {md_file} not found!")
        print(f"   Current directory: {os.getcwd()}")
        sys.exit(1)
    
    print(f"\n📄 Input: {md_file}")
    print(f"📄 Output: {pdf_file}\n")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Try weasyprint first
    try:
        import weasyprint
        if convert_with_weasyprint(md_file, pdf_file):
            print(f"\n📁 PDF saved to: {os.path.abspath(pdf_file)}")
            sys.exit(0)
    except ImportError:
        pass
    
    # Try pandoc as alternative
    try:
        import pypandoc
        if convert_with_pandoc(md_file, pdf_file):
            print(f"\n📁 PDF saved to: {os.path.abspath(pdf_file)}")
            sys.exit(0)
    except ImportError:
        pass
    
    # If both fail, provide manual instructions
    print("\n" + "="*70)
    print("MANUAL CONVERSION INSTRUCTIONS")
    print("="*70)
    print("\nOption 1: Use Pandoc (recommended for best quality)")
    print("  Install: https://pandoc.org/installing.html")
    print(f"  Then run: pandoc {md_file} -o {pdf_file} --pdf-engine=xelatex --toc")
    print("\nOption 2: Use online converter")
    print("  Upload to: https://www.markdowntopdf.com/")
    print("\nOption 3: Use VS Code")
    print("  Install 'Markdown PDF' extension")
    print("  Right-click markdown file → 'Markdown PDF: Export (pdf)'")
    print("\nOption 4: Install Python packages")
    print("  pip install weasyprint markdown2")
    print("  python generate_pdf_documentation.py")
    print("="*70)

if __name__ == "__main__":
    main()

