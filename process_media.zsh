#!/bin/zsh

# Before running, install these libraries using brew: 
# brew install ffmpeg imagemagick

# Base directory for mixed media files and sorted media
base_directory="~/"

# Subdirectories for sorted media
image_directory="$base_directory/images"
video_directory="$base_directory/videos"
gif_directory="$base_directory/gifs"

# Ensure the directories exist
mkdir -p "$image_directory" "$video_directory" "$gif_directory"

# Function to initialize counter based on the highest filename number in a directory
init_counter() {
  local directory=$1
  
  # Get the highest numbered filename in the directory, adding 1 for the next file
  local next_num=$(ls $directory | awk -F '.' '{print $1}' | sort -nr | head -n1)
  
  # If no files are found, start from 1; otherwise, increment the highest number found
  if [[ -z "$next_num" ]]; then
    echo 1
  else
    echo $((next_num + 1))
  fi
}

# Initialize counters for each type of media
image_counter=$(init_counter $image_directory)
video_counter=$(init_counter $video_directory)
gif_counter=$(init_counter $gif_directory)

# Function to process and move files
process_and_move_files() {
  for file in $base_directory/*.*; do
    # Skip directories
    [[ -d $file ]] && continue

    # Handle case-insensitive file extensions
    local extension="${file##*.}"
    local extension_lower=$(echo "$extension" | tr '[:upper:]' '[:lower:]')

    case $extension_lower in
      jpg|jpeg|png|tif|tiff|bmp)
        local target="${image_directory}/${image_counter}.jpg"
        convert "$file" "$target"
        ((image_counter++))
        ;;
      mp4|mov|avi|mkv|webm)
        local target="${video_directory}/${video_counter}.mp4"
        ffmpeg -i "$file" -c:v libx264 -pix_fmt yuv420p -preset slow -crf 22 -c:a aac -b:a 128k "$target"
        ((video_counter++))
        ;;
      gif)
        local target="${gif_directory}/${gif_counter}.gif"
        mv "$file" "$target"
        ((gif_counter++))
        ;;
    esac

    # Optionally, remove the original file after processing
    rm "$file"
  done
}

# Call the function to start processing the files
process_and_move_files
