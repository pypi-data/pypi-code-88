

VERSION_ID = "___VERSION_ID___"
CAPTION = "___CAPTION___"
LABEL = "___LABEL___"
IMAGE_LATEX_SNIPPET = rf"""\begin{{figure}}[h]
  \centering
  \includegraphics[\linewidth]{{{VERSION_ID}}}
  \caption{{{CAPTION}}}
  \label{{{LABEL}}}
\end{{figure}}
"""
