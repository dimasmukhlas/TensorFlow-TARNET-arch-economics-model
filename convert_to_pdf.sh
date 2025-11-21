#!/bin/bash
# Simple script to convert markdown to PDF using different methods

echo "=" | cat - <(echo "70") | tr -d '\n' | head -c 70 && echo ""
echo "TARNET DOCUMENTATION → PDF CONVERTER"
echo "=" | cat - <(echo "70") | tr -d '\n' | head -c 70 && echo ""

MD_FILE="TARNET_Project_Documentation.md"
PDF_FILE="TARNET_Project_Documentation.pdf"

# Method 1: Try pandoc with pdflatex (if available)
if command -v pandoc &> /dev/null && command -v pdflatex &> /dev/null; then
    echo "📄 Using pandoc with pdflatex..."
    pandoc "$MD_FILE" -o "$PDF_FILE" \
        --pdf-engine=pdflatex \
        --toc \
        --variable=geometry:margin=2cm \
        --highlight-style=tango
    if [ -f "$PDF_FILE" ]; then
        echo "✅ PDF generated: $PDF_FILE"
        exit 0
    fi
fi

# Method 2: Try pandoc with context (if available)
if command -v pandoc &> /dev/null && command -v context &> /dev/null; then
    echo "📄 Using pandoc with context..."
    pandoc "$MD_FILE" -o "$PDF_FILE" \
        --pdf-engine=context \
        --toc
    if [ -f "$PDF_FILE" ]; then
        echo "✅ PDF generated: $PDF_FILE"
        exit 0
    fi
fi

# Method 3: Try pandoc with latexmk (if available)
if command -v pandoc &> /dev/null && command -v latexmk &> /dev/null; then
    echo "📄 Using pandoc with latexmk..."
    pandoc "$MD_FILE" -o "$PDF_FILE" \
        --pdf-engine=latexmk \
        --toc \
        --variable=geometry:margin=2cm
    if [ -f "$PDF_FILE" ]; then
        echo "✅ PDF generated: $PDF_FILE"
        exit 0
    fi
fi

# If pandoc is available but no engine works, suggest installation
if command -v pandoc &> /dev/null; then
    echo ""
    echo "❌ Pandoc found but no PDF engine available"
    echo ""
    echo "To install xelatex on macOS:"
    echo "  brew install basictex"
    echo "  # Then add to PATH: export PATH=\"/Library/TeX/texbin:\$PATH\""
    echo ""
    echo "Or use pandoc without xelatex (HTML output):"
    pandoc "$MD_FILE" -o "${PDF_FILE%.pdf}.html" --standalone --toc
    echo "✅ HTML generated: ${PDF_FILE%.pdf}.html"
    echo "   Open in browser and print to PDF (Cmd+P → Save as PDF)"
else
    echo ""
    echo "❌ Pandoc not found"
    echo ""
    echo "Install pandoc:"
    echo "  brew install pandoc"
    echo ""
    echo "Then install a PDF engine:"
    echo "  brew install basictex  # For xelatex"
fi

echo ""
echo "=" | cat - <(echo "70") | tr -d '\n' | head -c 70 && echo ""
echo "ALTERNATIVE: Use online converter"
echo "=" | cat - <(echo "70") | tr -d '\n' | head -c 70 && echo ""
echo "1. Go to: https://www.markdowntopdf.com/"
echo "2. Upload: $MD_FILE"
echo "3. Download the PDF"
echo ""

