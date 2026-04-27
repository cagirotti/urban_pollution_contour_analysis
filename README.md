# urban_pollution_contour_analysis
Pipeline genérico para análise espaço-temporal da poluição urbana via contour plots (mês × hora). Generic pipeline for spatiotemporal analysis of urban air pollution using contour plots (month × hour).

## Requirements

Install dependencies:

pip install -r requirements.txt

## Usage

python src/run_analysis.py

## Input data

Datasets must include the following columns:

- data (date)
- hora (time, HH:MM:SS)
- pm10 (or pollutant of interest)
- vv (wind speed)
- blh (boundary layer height)
- instabilidade (atmospheric stability)
- temperature
- precipitation

## Notes

- Input data are not included
- Users must provide their own datasets
- Column names may require adaptation depending on the dataset

## Citation

This repository contains code developed for the study:

Girotti, C. et al. (2025). *Air pollution dynamics: The role of meteorological factors in PM10 concentration patterns across urban areas*. City and Environment Interactions, 25, 100184. https://doi.org/10.1016/j.cacint.2024.100184

The study analyzes the influence of meteorological variables such as wind speed, boundary layer height, and atmospheric stability on PM10 concentrations in urban environments :contentReference[oaicite:0]{index=0}.

If this code contributes to your work, please cite the article.

