#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2021 Kazuhiro KOBAYASHI <root.4mac@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from .layer import Conv1d, ConvLayers


class CCepLTVFilter(nn.Module):
    def __init__(
        self,
        in_channels,
        conv_channels=256,
        ccep_size=222,
        kernel_size=3,
        dilation_size=1,
        group_size=8,
        fft_size=1024,
        hop_size=256,
        n_ltv_layers=3,
        use_causal=False,
        conv_type="original",
        feat2linear_fn=None,
        ltv_postfilter_type="conv",
    ):
        super().__init__()
        self.fft_size = fft_size
        self.hop_size = hop_size
        # TODO(k2kobayashi): support overlap size not only 50%
        self.window_size = hop_size * 2
        self.ccep_size = ccep_size
        self.use_causal = use_causal
        self.feat2linear_fn = feat2linear_fn
        self.ltv_postfilter_type = ltv_postfilter_type

        win_norm = self.window_size // (hop_size * 2)  # only for hanning window
        self.win = torch.hann_window(self.window_size) / win_norm
        self.conv = ConvLayers(
            in_channels=in_channels,
            conv_channels=conv_channels,
            out_channels=ccep_size,
            kernel_size=kernel_size,
            dilation_size=dilation_size,
            group_size=group_size,
            n_conv_layers=n_ltv_layers,
            use_causal=use_causal,
            conv_type=conv_type,
        )
        idx = torch.arange(1, ccep_size // 2 + 1).float()
        self.quef_norm = torch.cat([torch.flip(idx, dims=[-1]), idx], dim=-1)

        # conv post filter
        self.ltv_postfilter_fn = self._get_ltv_postfilter_fn()

    def forward(self, x, z):
        """
        x: B, T, D
        z: B, 1, T * hop_size
        """

        # inference complex cepstrum
        ccep = self.conv(x)
        ccep = ccep / self.quef_norm.to(ccep.device)

        # apply LTV filter and overlap
        log_mag = None if self.feat2linear_fn is None else self.feat2linear_fn(x)
        y = self._ccep2impulse(ccep, ref=log_mag)
        z = self._conv_impulse(z, y)
        z = self._ola(z)

        if self.ltv_postfilter_fn is not None:
            z = self.ltv_postfilter_fn(z.transpose(1, 2)).transpose(1, 2)
        return z

    def _ccep2impulse(self, ccep, ref=None):
        padding = (self.fft_size - self.ccep_size) // 2
        ccep = F.pad(ccep, (padding, padding))
        y = torch.fft.fft(ccep, n=self.fft_size, dim=-1)
        if ref is not None:
            # TODO(k2kobayashi): it requires to consider following line.
            # this mask eliminates very small amplitude values (-100).
            # ref = ref * (ref > -100)
            y.real[..., : self.fft_size // 2 + 1] += ref
            y.real[..., self.fft_size // 2 :] += torch.flip(ref[..., 1:], dims=[-1])

        # NOTE(k2kobayashi): we assume intermidiate log amplitude as 10log10|mag|
        mag, phase = torch.pow(10, y.real / 10), y.imag
        real, imag = mag * torch.cos(phase), mag * torch.sin(phase)
        y = torch.fft.ifft(torch.complex(real, imag), n=self.fft_size, dim=-1)
        return y.real

    def _conv_impulse(self, z, y):
        z = z.reshape(z.size(0), 1, -1)  # (B, 1, T x hop_size)
        z = F.pad(z, (self.window_size // 2 - 1, self.window_size // 2))
        z = z.unfold(-1, self.window_size, step=self.hop_size)  # (B, 1, T, window_size)

        z = F.pad(z, (self.fft_size // 2 - 1, self.fft_size // 2))
        z = z.unfold(-1, self.fft_size, step=1)  # (B, 1, T, window_size, fft_size)

        # z = matmul(z, y) -> (B, 1, T, window_size) where
        # z: (B, 1, T, window_size, fft_size)
        # y: (B, T, fft_size) -> (B, 1, T, fft_size, 1)
        z = torch.matmul(z, y.unsqueeze(1).unsqueeze(-1)).squeeze(-1)
        return z

    def _ola(self, z):
        z = z * self.win.to(z.device)
        l, r = torch.chunk(z, 2, dim=-1)  # (B, 1, T, window_size // 2)
        z = l + torch.roll(r, 1, dims=2)  # roll a frame of right side
        z = z.reshape(z.size(0), 1, -1)
        return z

    def _get_ltv_postfilter_fn(self):
        # NOTE(k2kobayashi): no lookahead for LTV postfilter
        if self.ltv_postfilter_type == "ddsconv":
            fn = ConvLayers(
                in_channels=1,
                conv_channels=64,
                out_channels=1,
                kernel_size=5,
                dilation_size=2,
                n_conv_layers=self.n_postfilter_layers,
                look_ahead=0,
                use_causal=self.use_causal,
                conv_type="ddsconv",
            )
        elif self.ltv_postfilter_type == "conv":
            fn = Conv1d(
                in_channels=1,
                out_channels=1,
                kernel_size=self.fft_size,
                use_causal=self.use_causal,
                look_ahead=0,
            )
        elif self.ltv_postfilter_type is None:
            fn = None
        else:
            raise ValueError(f"Invalid ltv_postfilter_type: {self.ltv_postfilter_type}")
        return fn


class SinusoidsGenerator(nn.Module):
    def __init__(
        self,
        hop_size,
        fs=24000,
        harmonic_amp=0.1,
        noise_std=0.03,
        n_harmonics=200,
        use_uvmask=True,
    ):
        super().__init__()
        self.fs = fs
        self.harmonic_amp = harmonic_amp
        self.noise_std = noise_std
        self.upsample = nn.Upsample(scale_factor=hop_size, mode="nearest")
        self.use_uvmask = True

        self.n_harmonics = n_harmonics
        self.harmonics = torch.arange(1, self.n_harmonics + 1).unsqueeze(-1)

    def forward(self, cf0, uv):
        device = cf0.device
        f0, uv = self.upsample(cf0.transpose(1, 2)), self.upsample(uv.transpose(1, 2))
        harmonic = self.generate_sinusoids(f0, uv).reshape(cf0.size(0), 1, -1)
        noise = torch.normal(0, self.noise_std, size=harmonic.size()).to(device)
        return harmonic, noise

    def generate_sinusoids(self, f0, uv):
        harmonics = self.harmonics.to(f0.device)
        mask = self.anti_aliacing_mask(f0 * harmonics)
        rads = f0.cumsum(dim=-1) * 2.0 * math.pi / self.fs * harmonics
        harmonic = torch.sum(torch.cos(rads) * mask, dim=1, keepdim=True)
        if self.use_uvmask:
            harmonic = uv * harmonic
        return self.harmonic_amp * harmonic

    def anti_aliacing_mask(self, f0_with_harmonics, use_soft_mask=False):
        if use_soft_mask:
            return torch.sigmoid(-(f0_with_harmonics - self.fs / 2.0))
        else:
            return (f0_with_harmonics < self.fs / 2.0).float()
