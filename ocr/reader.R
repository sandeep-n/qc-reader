library(magrittr)
library(magick)
library(curl)
library(tesseract)

img_dir <- "C:/Users/sande/Projects/qc-reader/test-data/panels"
img_file <- "C:/Users/sande/Projects/qc-reader/test-data/panels/qc3562-1.png"

# Plain old tesseract
text <- ocr(img_file)
print(text)

# With magick
text <- image_read(img_file) %>%
  image_convert(colorspace = 'gray') %>%
  image_trim() %>%
  image_ocr()
print(text)

