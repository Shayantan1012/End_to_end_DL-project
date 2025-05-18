import io
print("-----------------------------------------------------------------------")
import bentoml
import numpy as np
import torch
from Xray.ml.model.arch import Net
from bentoml.io import Image, Text
from PIL import Image as PILImage

from Xray.constant.TrainingPipeline import *

# bento_model = bentoml.pytorch.load_model(BENTOML_MODEL_NAME)

# torch.serialization.add_safe_globals({'Xray.ml.model.arch.Net': Net})

# bento_model = bentoml.pytorch.load_model(BENTOML_MODEL_NAME)


bento_model = bentoml.pytorch.get(BENTOML_MODEL_NAME)

runner = bento_model.to_runner()

svc = bentoml.Service(name=BENTOML_SERVICE_NAME, runners=[runner])

print("Loaded model:", bento_model)
print("Custom objects:", bento_model.custom_objects)
print("Transform key found:", TRAIN_TRANSFORMS_KEY in bento_model.custom_objects)
# print("Running prediction on image with shape:", image.shape)


@svc.api(input=Image(allowed_mime_types=["image/jpeg"]), output=Text())

async def predict(img):
    b = io.BytesIO()

    img.save(b, "jpeg")

    im_bytes = b.getvalue()

    my_transforms = bento_model.custom_objects.get(TRAIN_TRANSFORMS_KEY)

    image = PILImage.open(io.BytesIO(im_bytes)).convert("RGB")

    
    image = my_transforms(image).unsqueeze(0)


    batch_ret = await runner.async_run(image)

    pred = PREDICTION_LABEL[max(torch.argmax(batch_ret, dim=1).detach().cpu().tolist())]

    return pred


# import io
# print("-----------------------------------------------------------------------")
# import bentoml
# import numpy as np
# import torch
# from bentoml.io import Image, Text
# from PIL import Image as PILImage

# from Xray.constant.TrainingPipeline import *
  # ✅ Import your Net class

# # ✅ Whitelist the Net class to allow safe unpickling


# # ✅ Load the full model, explicitly saying weights_only=False
# 

# runner = bento_model.to_runner()

# svc = bentoml.Service(name=BENTOML_SERVICE_NAME, runners=[runner])

# print("Loaded model:", bento_model)
# print("Custom objects:", bento_model.custom_objects)
# print("Transform key found:", TRAIN_TRANSFORMS_KEY in bento_model.custom_objects)

# @svc.api(input=Image(allowed_mime_types=["image/jpeg"]), output=Text())
# async def predict(img):
#     b = io.BytesIO()
#     img.save(b, "jpeg")
#     im_bytes = b.getvalue()

#     my_transforms = bento_model.custom_objects.get(TRAIN_TRANSFORMS_KEY)

#     image = PILImage.open(io.BytesIO(im_bytes)).convert("RGB")
#     image = my_transforms(image).unsqueeze(0)

#     batch_ret = await runner.async_run(image)

#     pred = PREDICTION_LABEL[max(torch.argmax(batch_ret, dim=1).detach().cpu().tolist())]

#     return pred
