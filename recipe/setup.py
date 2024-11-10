# Copyright (c) 2023, Tri Dao.
# Copyright (c) 2024, Conda-forge Contributors.

"""Since this package is a pytorch extension, this setup file uses the custom
CUDAExtension build system from pytorch. This ensures that compatible compiler
args, headers, etc for pytorch.

Read more at the pytorch docs:
https://pytorch.org/docs/stable/cpp_extension.html#torch.utils.cpp_extension.CUDAExtension
"""

import pathlib
import sys

from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

_this_dir = pathlib.Path(__file__).parent.absolute()

setup(
    packages=find_packages(
        include=["flash_attn*"],
    ),
    ext_modules=[
        CUDAExtension(
            name="flash_attn_2_cuda",
            sources=[
                "csrc/flash_attn/flash_api.cpp",
                "csrc/flash_attn/src/flash_fwd_hdim32_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim32_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim64_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim64_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim96_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim96_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim128_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim128_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim160_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim160_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim192_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim192_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim256_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim256_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim32_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim32_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim64_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim64_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim96_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim96_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim128_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim128_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim160_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim160_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim192_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim192_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim256_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_hdim256_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim32_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim32_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim64_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim64_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim96_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim96_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim128_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim128_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim160_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim160_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim192_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim192_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim256_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim256_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim32_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim32_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim64_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim64_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim96_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim96_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim128_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim128_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim160_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim160_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim192_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim192_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim256_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_bwd_hdim256_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim32_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim32_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim64_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim64_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim96_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim96_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim128_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim128_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim160_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim192_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim192_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim256_fp16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim256_bf16_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim32_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim32_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim64_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim64_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim96_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim96_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim128_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim128_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim160_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim192_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim192_bf16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim256_fp16_causal_sm80.cu",
                "csrc/flash_attn/src/flash_fwd_split_hdim256_bf16_causal_sm80.cu",
            ],
            extra_compile_args={
                "cxx": ["-std=c++17"],
                "nvcc": [
                    "-std=c++17",
                    "-U__CUDA_NO_HALF_OPERATORS__",
                    "-U__CUDA_NO_HALF_CONVERSIONS__",
                    "-U__CUDA_NO_HALF2_OPERATORS__",
                    "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
                    "--expt-relaxed-constexpr",
                    "--expt-extended-lambda",
                    "--use_fast_math",
                    # "--ptxas-options=-v",
                    # "--ptxas-options=-O2",
                    # "-lineinfo",
                    # "-DFLASHATTENTION_DISABLE_BACKWARD",
                    # "-DFLASHATTENTION_DISABLE_DROPOUT",
                    # "-DFLASHATTENTION_DISABLE_ALIBI",
                    # "-DFLASHATTENTION_DISABLE_SOFTCAP",
                    # "-DFLASHATTENTION_DISABLE_UNEVEN_K",
                    # "-DFLASHATTENTION_DISABLE_LOCAL",
                ],
            },
            extra_link_args=["-Wl,--strip-all", "-Wl,--no-undefined"],
            include_dirs=[
                _this_dir / "csrc" / "flash_attn",
                _this_dir / "csrc" / "flash_attn" / "src",
                _this_dir / "csrc" / "cutlass" / "include",
            ],
            libraries=[
                "cudart",
                f"python{sys.version_info[0]}.{sys.version_info[1]}",
            ],
        ),
        CUDAExtension(
            name="fused_dense_lib",
            sources=[
                "csrc/fused_dense_lib/fused_dense.cpp",
                "csrc/fused_dense_lib/fused_dense_cuda.cu",
            ],
            extra_compile_args={
                "cxx": [
                    "-O3",
                ],
                "nvcc": ["-O3"],
            },
            extra_link_args=["-Wl,--strip-all", "-Wl,--no-undefined"],
            libraries=[
                "cudart",
                "cublas",
                "cublasLt",
                f"python{sys.version_info[0]}.{sys.version_info[1]}",
            ],
        ),
        CUDAExtension(
            name="dropout_layer_norm",
            sources=[
                "csrc/layer_norm/ln_api.cpp",
                "csrc/layer_norm/ln_fwd_256.cu",
                "csrc/layer_norm/ln_bwd_256.cu",
                "csrc/layer_norm/ln_fwd_512.cu",
                "csrc/layer_norm/ln_bwd_512.cu",
                "csrc/layer_norm/ln_fwd_768.cu",
                "csrc/layer_norm/ln_bwd_768.cu",
                "csrc/layer_norm/ln_fwd_1024.cu",
                "csrc/layer_norm/ln_bwd_1024.cu",
                "csrc/layer_norm/ln_fwd_1280.cu",
                "csrc/layer_norm/ln_bwd_1280.cu",
                "csrc/layer_norm/ln_fwd_1536.cu",
                "csrc/layer_norm/ln_bwd_1536.cu",
                "csrc/layer_norm/ln_fwd_2048.cu",
                "csrc/layer_norm/ln_bwd_2048.cu",
                "csrc/layer_norm/ln_fwd_2560.cu",
                "csrc/layer_norm/ln_bwd_2560.cu",
                "csrc/layer_norm/ln_fwd_3072.cu",
                "csrc/layer_norm/ln_bwd_3072.cu",
                "csrc/layer_norm/ln_fwd_4096.cu",
                "csrc/layer_norm/ln_bwd_4096.cu",
                "csrc/layer_norm/ln_fwd_5120.cu",
                "csrc/layer_norm/ln_bwd_5120.cu",
                "csrc/layer_norm/ln_fwd_6144.cu",
                "csrc/layer_norm/ln_bwd_6144.cu",
                "csrc/layer_norm/ln_fwd_7168.cu",
                "csrc/layer_norm/ln_bwd_7168.cu",
                "csrc/layer_norm/ln_fwd_8192.cu",
                "csrc/layer_norm/ln_bwd_8192.cu",
                "csrc/layer_norm/ln_parallel_fwd_256.cu",
                "csrc/layer_norm/ln_parallel_bwd_256.cu",
                "csrc/layer_norm/ln_parallel_fwd_512.cu",
                "csrc/layer_norm/ln_parallel_bwd_512.cu",
                "csrc/layer_norm/ln_parallel_fwd_768.cu",
                "csrc/layer_norm/ln_parallel_bwd_768.cu",
                "csrc/layer_norm/ln_parallel_fwd_1024.cu",
                "csrc/layer_norm/ln_parallel_bwd_1024.cu",
                "csrc/layer_norm/ln_parallel_fwd_1280.cu",
                "csrc/layer_norm/ln_parallel_bwd_1280.cu",
                "csrc/layer_norm/ln_parallel_fwd_1536.cu",
                "csrc/layer_norm/ln_parallel_bwd_1536.cu",
                "csrc/layer_norm/ln_parallel_fwd_2048.cu",
                "csrc/layer_norm/ln_parallel_bwd_2048.cu",
                "csrc/layer_norm/ln_parallel_fwd_2560.cu",
                "csrc/layer_norm/ln_parallel_bwd_2560.cu",
                "csrc/layer_norm/ln_parallel_fwd_3072.cu",
                "csrc/layer_norm/ln_parallel_bwd_3072.cu",
                "csrc/layer_norm/ln_parallel_fwd_4096.cu",
                "csrc/layer_norm/ln_parallel_bwd_4096.cu",
                "csrc/layer_norm/ln_parallel_fwd_5120.cu",
                "csrc/layer_norm/ln_parallel_bwd_5120.cu",
                "csrc/layer_norm/ln_parallel_fwd_6144.cu",
                "csrc/layer_norm/ln_parallel_bwd_6144.cu",
                "csrc/layer_norm/ln_parallel_fwd_7168.cu",
                "csrc/layer_norm/ln_parallel_bwd_7168.cu",
                "csrc/layer_norm/ln_parallel_fwd_8192.cu",
                "csrc/layer_norm/ln_parallel_bwd_8192.cu",
            ],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": [
                    "-O3",
                    "-U__CUDA_NO_HALF_OPERATORS__",
                    "-U__CUDA_NO_HALF_CONVERSIONS__",
                    "-U__CUDA_NO_BFLOAT16_OPERATORS__",
                    "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
                    "-U__CUDA_NO_BFLOAT162_OPERATORS__",
                    "-U__CUDA_NO_BFLOAT162_CONVERSIONS__",
                    "--expt-relaxed-constexpr",
                    "--expt-extended-lambda",
                    "--use_fast_math",
                ],
            },
            extra_link_args=["-Wl,--strip-all", "-Wl,--no-undefined"],
            include_dirs=[
                _this_dir / "csrc" / "layer_norm",
            ],
            libraries=[
                "cudart",
                f"python{sys.version_info[0]}.{sys.version_info[1]}",
            ],
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
    zip_safe=False,
)
