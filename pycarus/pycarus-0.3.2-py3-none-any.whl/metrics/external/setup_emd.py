from setuptools import setup  # type: ignore
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="emd",
    ext_modules=[
        CUDAExtension(  # type: ignore
            "emd",
            [
                "/".join(__file__.split("/")[:-1] + ["emd.cpp"]),
                "/".join(__file__.split("/")[:-1] + ["emd_cuda.cu"]),
            ],
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
)
