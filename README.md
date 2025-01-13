# Nord Wallpaper Converter

A Python script that efficiently converts images to use the [Nord color palette](https://www.nordtheme.com/). This tool is optimized for systems with integrated graphics and moderate RAM, making it perfect for converting wallpapers and images on standard desktop computers.

![Nord Color Palette](https://raw.githubusercontent.com/nordtheme/assets/main/static/images/logos/heroes/logo-typography/light/frostic/nord6/spaced.svg?sanitize=true)

## Features

- 🎨 Converts images to use the Nord color palette
- 📦 Supports multiple image formats (JPG, PNG, WEBP, BMP)
- 🚀 Optimized for systems with integrated graphics
- 💾 Memory-efficient processing with dynamic chunk sizing
- ⚡ Multi-threaded processing for better performance
- 📊 Progress tracking with estimated time remaining
- 🔄 Handles transparent images (PNG, WEBP)
- 📈 Automatically adjusts to your system's capabilities

## Requirements

- Python 3.7 or higher
- 8GB RAM (minimum)
- Intel i5 8th gen or equivalent processor
- Integrated or discrete graphics

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/nord-wallpaper-converter.git
cd nord-wallpaper-converter
```

2. Install required packages:
```bash
# use venv or virtualenv to create virtual environment
python -m venv myenv
source myenv/bin/activate
pip install Pillow numpy tqdm psutil
```

## Usage

### Basic Usage

Run the script from command line:
```bash
python nord_converter.py "input_folder" "output_folder"
```

Example:
```bash
python nord_converter.py "C:/Users/YourName/Pictures/Wallpapers" "C:/Users/YourName/Pictures/Wallpapers_Nord"
```

### Progress Tracking

The script shows a progress bar with:
- Number of images processed
- Estimated time remaining
- Current processing speed
- Available system memory

## How It Works

1. **Image Loading**: Loads each image and handles transparency if present
2. **Color Conversion**: Uses vectorized operations to match each pixel to the closest Nord color
3. **Memory Management**: 
   - Processes images in chunks to prevent memory overflow
   - Dynamically adjusts chunk size based on available system memory
   - Uses garbage collection to maintain stable memory usage
4. **Multi-threading**: 
   - Automatically determines optimal number of worker threads
   - Bases thread count on available CPU cores and memory
5. **Output**: Saves processed images in their original format with Nord colors

## Nord Color Palette

The converter uses the official Nord color palette:
- Polar Night (dark greys/blacks)
- Snow Storm (light greys/whites)
- Frost (blue-tinted whites)
- Aurora (vibrant accent colors)

## Performance

Performance varies based on:
- Image size and quantity
- Available RAM
- CPU speed
- Storage speed (SSD/HDD)

Typical processing times:
- 1080p wallpaper: 2-5 seconds
- 4K wallpaper: 5-10 seconds

## Known Limitations

- Large images (>4K) may require additional processing time
- Processing speed depends on available system memory
- Some very large images might be automatically downsized to prevent memory issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Nord Theme](https://www.nordtheme.com/) for the color palette
- The Python Pillow team for the image processing library
- NumPy team for the efficient array operations

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues on GitHub
2. Create a new issue with details about your problem
3. Include your system specifications and any error messages

---

Made with ❄️ by [Aman Kumar Gupta]
