(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "inputenc"
    "blindtext"
    "graphicx"
    "amsmath"
    "csvsimple"
    "pdfpages"
    "hyperref"
    "gensymb")
   (LaTeX-add-labels
    "eq:B"
    "eq:r"
    "eq:qm"
    "eq:deb"
    "eq:kin"
    "eq:lam"
    "eq:dif"
    "eq:tan"
    "eq:final")
   (LaTeX-add-bibitems
    "r:qm"
    "r:em"
    "r:hc"))
 :latex)

