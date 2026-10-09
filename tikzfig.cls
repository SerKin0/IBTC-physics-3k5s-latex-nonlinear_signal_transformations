\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tikzfigure}[2026/10/09 Standalone TikZ figures]

% Базовый класс: PDF автоматически обрезается по содержимому
\LoadClass[tikz,border=2pt]{standalone}

% --------------------------------------------------
% Кодировка и русский язык (pdfLaTeX)
% --------------------------------------------------

\RequirePackage{cmap}
\RequirePackage[T2A]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[english,russian]{babel}
\RequirePackage{microtype}

% --------------------------------------------------
% Математика
% --------------------------------------------------

\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsfonts}
\RequirePackage{mathtools}
\RequirePackage{icomma}

% --------------------------------------------------
% Графика и схемы
% --------------------------------------------------

\RequirePackage{tikz}
\usetikzlibrary{
    arrows.meta,
    calc,
    positioning,
    angles,
    quotes,
    patterns,
    intersections
}

\RequirePackage{circuitikz}

\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}

% --------------------------------------------------
% Общие настройки
% --------------------------------------------------

\pagestyle{empty}
\setlength{\parindent}{0pt}

\endinput