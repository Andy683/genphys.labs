\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lab_class}
\ProcessOptions

\LoadClass[a4paper,12pt]{article}

\RequirePackage[T2A]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[english,russian]{babel}

\RequirePackage{amsfonts,amssymb,amsthm,mathtools,mathrsfs}
\RequirePackage{physics}
\RequirePackage{wrapfig,graphicx,float}
\RequirePackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=1.0cm,includefoot,footskip=1.0cm]{geometry}

% additional useful commands 
\newcommand{\const}{\text{const}}
\newcommand{\then}{\quad\Rightarrow\quad}

\input{../units.cls}