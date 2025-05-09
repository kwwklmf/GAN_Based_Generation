import zipfile

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# 使用示例
unzip_file('/home/kongweiwen/github_code/pytorch-CycleGAN-and-pix2pix/datasets/pix2pix_dataset.zip', '/home/kongweiwen/github_code/pytorch-CycleGAN-and-pix2pix/datasets/cars')