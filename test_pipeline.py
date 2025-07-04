
from src.extract_frames import extract_frames
from src.optical_flow import compute_optical_flow

# Caminho do vídeo de entrada
video_path = 'data/videos/sample.mp4'

# Diretórios de saída
frames_output_dir = 'data/frames'
flow_output_dir = 'output/flow'

# Extração de frames
extract_frames(video_path, frames_output_dir, max_frames=200)

# Cálculo de fluxo óptico
compute_optical_flow(frames_output_dir, flow_output_dir)
