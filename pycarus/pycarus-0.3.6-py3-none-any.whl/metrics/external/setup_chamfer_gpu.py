from setuptools import setup  # type: ignore
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="chamfer_cuda",
    ext_modules=[
        CUDAExtension(  # type: ignore
            "chamfer_cuda",
            [
                "/".join(__file__.split("/")[:-1] + ["chamfer_cuda.cpp"]),
                "/".join(__file__.split("/")[:-1] + ["chamfer_3D.cu"]),
            ],
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
)
