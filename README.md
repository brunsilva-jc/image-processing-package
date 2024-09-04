# Image Processing Package

Description. 
The package Image Processing is used to:
	
- Combine images and show the result on image format or histogram format
	

- Transform images scales

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install image-processing-brunsilvajc==0.0.1
```

## Usage

Combine two images
```python
from image_processing.processing import combination
from image_processing.utils import io, plot

image1 = io.read_image("path to the image1")
image2 = io.read_image("path to the image2")

comb_image = combination.transfer_histogram(image1, image2)

#show the image combination
plot.plot_result(image1, image2, comb_image)

#show the histogram related with the image combination
plot.plot_histogram(comb_image)
```

Transform an Image
```python
from image_processing.processing import transformation
from image_processing.utils import io, plot

image1 = io.read_image("path to the image1")

#first argument is an image, second argument is the proportion from 0 to 1
transformation.resize_image(image1, 0.5)
```

## Author
BrunSilva-JC

## License
[MIT](https://choosealicense.com/licenses/mit/)