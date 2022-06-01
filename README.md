# Analysis
## *Our Aim*

> We are going to calculate plant health on Earth and compare it to factors from NASA datasets and datasets we create, like air pollution, population density, temperature, humidity, daylight time, cloud cover, longitude and latitude, to get an idea of how limiting factors work on a large scale. This could help farmers maximise production and help analyse the reasons for deforestation, and help people find the optimal areas and conditions to plant crops or carry out reforestation.

## Dependencies

Please add any PIP-installed libraries here with their use:

| Dependency | Use                         |
|------------|-----------------------------|
| numpy      | Image processing & analysis |
| opencv     | Image processing            |
| skyfield   | ISS Location                |

## Datasets used

| Dataset               | Use                           |
|-----------------------|-------------------------------|
| ISLSCP_II_MODISLC_968 | Getting land cover categories |

## Notes

* Number of images to process:
  * Takes around 2.5 seconds to open (but not process) 100 photo pairs
  * We have 4146 photos
  * Therefore, opening all the images would take around 2 minutes
* Land/sea
  * Use location?
  * Then filter by colour?