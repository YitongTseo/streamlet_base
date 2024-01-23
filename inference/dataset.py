
from PIL import Image
from torchvision import transforms
import torchvision.transforms as transforms
from os import listdir
from os.path import isfile, join

class PneumoniaDataset(Dataset):
    def __init__(self, positive_dir, negative_dir, transform=None):
        positive_files = [join(positive_dir, f) for f in listdir(positive_dir) if isfile(join(positive_dir, f))]
        negative_files = [join(negative_dir, f) for f in listdir(negative_dir) if isfile(join(negative_dir, f))]

        self.X = positive_files + negative_files
        self.y = torch.vstack(
            (
                torch.ones((len(positive_files),1)),
                torch.zeros((len(negative_files),1))
            )
        )
        self.transform = transform


    def __len__(self):
        # return None # TODO: Fill out

        return len(self.X)

    def __getitem__(self, idx):
        image_path = self.X[idx]
        image = Image.open(image_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, self.y[idx]