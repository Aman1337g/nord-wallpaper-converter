# Nord Wallpaper Converter

A Python script that converts images to use the [Nord color palette](https://www.nordtheme.com/). Designed for systems with integrated graphics and moderate RAM, it’s perfect for converting wallpapers and images efficiently on standard desktop computers.

![Nord Color Palette](https://raw.githubusercontent.com/nordtheme/assets/main/static/images/logos/heroes/logo-typography/light/frostic/nord6/spaced.svg?sanitize=true)

---

## Features

- 🎨 Converts images to the Nord color palette
- 📦 Supports multiple image formats (JPG, PNG, WEBP, BMP)
- 🚀 Optimized for systems with integrated graphics
- 💾 Memory-efficient with dynamic chunk sizing
- ⚡ Multi-threaded processing for enhanced performance
- 📊 Real-time progress tracking with estimated time remaining
- 🔄 Handles transparency for PNG and WEBP formats
- 📈 Adjusts dynamically to your system’s capabilities

---

## Requirements

- **Python**: Version 3.7 or higher
- **System Specs**:
  - 8GB RAM (minimum)
  - Intel i5 8th gen or equivalent processor
  - Integrated or discrete graphics card

---

## Installation

### Option 1: Download the Prebuilt Binary

1. Download the executable from the [releases page](https://github.com/Aman1337g/nord-wallpaper-converter/releases).
2. Run the binary:
   ```bash
   ./nord_converter input_folder output_folder
   ```

### Option 2: Use `curl` to Run Directly (No Download Needed)

Run the following command in your terminal:
```bash
curl -Ls https://github.com/Aman1337g/nord-wallpaper-converter/releases/latest/download/nord_converter | bash -s input_folder output_folder
```

<details>
<summary><strong>Pro Tip: Create an Alias or Function</strong></summary>

#### Alias
Add this line to your shell configuration file (e.g., `.bashrc`, `.zshrc`):
```bash
alias nord_convert='curl -Ls https://github.com/Aman1337g/nord-wallpaper-converter/releases/latest/download/nord_converter | bash -s'
```

Run it like this:
```bash
nord_convert input_folder output_folder
```

#### Function
For more flexibility, use a shell function:
```bash
nord_convert() {
  curl -Ls https://github.com/Aman1337g/nord-wallpaper-converter/releases/latest/download/nord_converter | bash -s "$@"
}
```

Run it like this:
```bash
nord_convert input_folder output_folder
```
</details>

---

### Option 3: Build the Executable Yourself

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/Aman1337g/nord-wallpaper-converter.git
   cd nord-wallpaper-converter
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

2. Build the executable using `PyInstaller`:
   ```bash
   pyinstaller --onefile nord_converter.py
   ```

3. Run the executable:
   ```bash
   ./dist/nord_converter input_folder output_folder
   ```

---

## Usage

### Option 1: Using the Binary
```bash
./nord_converter input_folder output_folder
```

### Option 2: Running the Python Script Directly
```bash
python nord_converter.py "input_folder" "output_folder"
```

Example:
```bash
python nord_converter.py "/home/user/Pictures/Wallpapers" "/home/user/Pictures/Wallpapers_Nord"
```

---

## Progress Tracking

The script provides:
- Real-time progress updates
- Number of images processed
- Estimated time remaining
- Current processing speed
- Available system memory

---

## How It Works

1. **Image Loading**: Reads images and handles transparency.
2. **Color Conversion**: Maps pixels to the closest Nord colors using vectorized operations.
3. **Memory Management**:
   - Processes images in chunks to avoid memory overflow.
   - Dynamically adjusts chunk sizes based on available system memory.
4. **Multi-threading**:
   - Automatically determines the optimal number of threads based on your system.
5. **Output**: Saves images in their original format but with the Nord color palette.

---

## Performance

### Estimated Processing Times:
- **1080p wallpaper**: 2-5 seconds
- **4K wallpaper**: 5-10 seconds

**Factors affecting performance**:
- Image size and quantity
- System memory and CPU speed
- Storage type (SSD/HDD)

---

## Known Limitations

- Large images (>4K) may take additional processing time.
- Very large images might be downsized automatically to prevent memory issues.

---

## Contributing

Contributions are welcome! To get started:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/AmazingFeature`.
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`.
4. Push the branch: `git push origin feature/AmazingFeature`.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Nord Theme](https://www.nordtheme.com/) for the color palette.
- Python libraries like [Pillow](https://python-pillow.org/) and [NumPy](https://numpy.org/) for image processing and efficient array operations.

---

## Support

If you encounter issues:
1. Check the [GitHub Issues](https://github.com/Aman1337g/nord-wallpaper-converter/issues) page.
2. Open a new issue with details about your problem (system specs, error messages, etc.).

---

Made with ❄️ by Aman Kumar Gupta.
