# image_meta_data_extraction
The Indian Ocean Tuna Commission ([IOTC](http://www.iotc.org/)) requires each of it's member countries to properly regulate and document as much catch as possible from long line fishing. These fisheries usually catch species such as Yellowfin Tuna (*Thunnus albacares*), Mackerel Tuna (*Euthynnus affinis*), Sailfish and Swordfish species. The high value of these catches requires rigorous documentation including information on catch date, time, geolocation, vessel data, catch gear used and morphometrics.

In order to better comply with these standards, the Department of Fisheries of Sri Lanka issued a waterproof point and shoot camera to a long line fishing vessel and requested the crew to take photographs of each catch. The author volunteered to help extract the meta data stored in these images that will help conforming to the [IOTC catch reporting standards](http://iotc.org/sites/default/files/documents/data/Guidelines%20Data%20Reporting%20IOTC.pdf).
This repository contains code and associated files that were written by the author to help extract the date, time, and geolocation of images that will be taken by these vessles. This is still in development stage and more comprehensive testing and refactoring of the code will be required.

Over the next few weeks I will be adding some modules and codes that I will be using to extract some metadata from a set of images that were captured using a Nikon Coolpix W300 point and shoot camera.

## Requirements
1. Python 3.4+
2. PIL (Python Imaging Library) - pip install pillow

## Meta data that's stored in an image taken using a Nikon Coolpix W300
The following list has been extracted using the script named 'meta_data_description.py'
1. ExifVersion
2. ComponentsConfiguration
3. CompressedBitsPerPixel
4. DateTimeOriginal
5. DateTimeDigitized
6. MaxApertureValue
7. UserComment
8. MeteringMode
9. LightSource
10. Flash
11. FocalLength
12. SubjectDistanceRange
13. ExifImageWidth
14. ImageDescription
15. Make
16. Model
17. Orientation
18. YCbCrPositioning
19. Contrast
20. Copyright
21. ExposureBiasValue
22. XResolution
23. YResolution
24. ExposureTime
25. DigitalZoomRatio
26. ExifInteroperabilityOffset
27. ExposureProgram
28. ColorSpace
29. GPSInfo
30. ISOSpeedRatings
31. ResolutionUnit
32. WhiteBalance
33. GainControl
34. FNumber
35. Software
36. DateTime
37. Saturation
38. Artist
39. FocalLengthIn35mmFilm
40. Sharpness
41. FileSource
42. CustomRendered
43. FlashPixVersion
44. SceneType
45. SceneCaptureType
46. ExifImageHeight
47. ExposureMode
48. ExifOffset
49. MakerNote

