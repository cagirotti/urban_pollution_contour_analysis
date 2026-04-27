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

