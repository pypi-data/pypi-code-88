#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import binascii
import sys
import math
import time
import random
import logging
import coloredlogs
import itertools
import hashlib
import operator
import functools
import decimal
import fractions
from typing import Optional, Union
from bitarray import bitarray
from numpy.random import Generator, PCG64
from randomgen.aes import AESCounter
from randomgen.chacha import ChaCha
from rtt_data_gen.base import OutputSequencer

logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def comp_rejection_ratio(modulus, osize_interval):
    """Returns a probability that a random draw from [0, modulus) will be rejected when spreading
    to uniform distribution to [0, osize_interval). Holds only for modulus <= osize_interval"""
    tp = math.ceil(osize_interval / modulus) - 1  # number of full-sized ms inside the range
    return 1 / (tp + 1) * ((tp + 1) * modulus - osize_interval) / modulus


def randbytes(x):
    osize = 0
    r = bytearray(x)
    while osize < x:
        rest = x - osize
        ssize = 8 if rest >= 8 else rest
        z = random.getrandbits(ssize << 3)
        zb = z.to_bytes(ssize, 'big')
        for i in range(ssize):
            r[osize + i] = zb[i]
        osize += ssize
    return bytes(r)


def counter(offset=0, mod=None):
    ctr = offset
    while True:
        yield ctr
        ctr += 1
        if mod:
            ctr %= mod


def number_streamer(gen, osize, nbytes, endian='big'):
    osize_b = int(math.ceil(osize/8.))
    b = bitarray(endian=endian)
    btmp = bitarray(endian=endian)
    offset = osize_b * 8 - osize
    for x in itertools.islice(gen, nbytes*8 // osize):
        xb = int(x).to_bytes(osize_b, endian)
        btmp.clear()
        btmp.frombytes(xb)
        b += btmp[offset:]
    return b.tobytes()


class RGenerator:
    FLOAT_PREC = fractions.Fraction(1, 1 << 50)
    FLOAT_MULT = fractions.Fraction(1 << 50, 1)

    def __init__(self):
        pass

    def randint(self, low, high, size=None):
        raise ValueError()

    def randbytes(self, length):
        raise ValueError()

    def randbits(self, bits):
        raise ValueError()

    def uniform(self, low, high, size=None):
        raise ValueError()

    def random(self, size=None):
        raise ValueError()

    def normal(self, loc=0.0, scale=1.0, size=None):
        raise ValueError()

    def random_precise(self, precision: Union[None, int, float] = 50, size=None):
        """Returns fractional on [0,1) with given precision (large number computation). Double precision is 53 bits."""
        steps = math.ceil((precision or 50) / 50.)

        prec = 1 << 50
        ssize = size or 1
        single = size is None

        # 50-bit precision random values
        vals = (int(x * prec) for x in self.random(steps * ssize))
        res = [None] * ssize

        for oi in range(ssize):
            cres = 0
            sub = 0
            for i in range(steps):
                cres += next(vals) << sub
                sub += 50
            cres = fractions.Fraction(cres, 1 << sub, _normalize=False)

            if single:
                return cres
            res[oi] = cres
        return res

    def uniform_precise(self, low, high, size=None, precision: Union[int, float] = 50):
        mag = high - low
        if size is None:
            return low + self.random_precise(precision, size) * mag

        return [low + (x * mag) for x in self.random_precise(precision, size)]


class RGeneratorRandom(RGenerator):
    def __init__(self, seed=None):
        super().__init__()
        if seed:
            random.seed(seed)

    def randint(self, low, high, size=None):
        if size is None:
            return random.randint(low, high)
        return [random.randint(low, high) for _ in range(size)]

    def randbytes(self, length):
        return randbytes(length)

    def randbits(self, bits):
        return random.getrandbits(bits)

    def uniform(self, low, high, size=None):
        if size is None:
            return random.uniform(low, high)
        return [random.uniform(low, high) for _ in range(size)]

    def random(self, size=None):
        if size is None:
            return random.random()
        return [random.random() for _ in range(size)]


def log2ceil(x):
    cd = math.ceil(math.log(x, 2))
    return cd if x <= 2**cd else cd+1


class RGeneratorPCG(RGenerator):
    INT64_LIMIT = 2**63
    DOUBLE_LIMIT = 2**53

    def __init__(self, seed=None, cls=None, cls_kw=None):
        super().__init__()
        seedx = int.from_bytes(bytes=seed, byteorder='big') if seed else None
        self.rand = PCG64(seedx) if cls is None else cls(seedx, **(cls_kw or {}))
        self.gen = Generator(self.rand)
        self.warned_high_inv = False
        self.warned_high_uni = False

    def randint(self, low, high, size=None):
        if high >= self.INT64_LIMIT:
            return self.randint_bytes_rejection(low, high, size)

        # high is too high for some moduli, >= 2**64
        return [int(x) for x in self.gen.integers(low, high, size=size, endpoint=True)]

    def randint_bytes_rejection(self, low, high, size=None):
        """Generates large random integers, above 2**63, using rejection sampling from random bytes"""
        res = []
        single = size is None

        mag = high - low
        big_mag = mag >= self.INT64_LIMIT
        if mag == 0:
            sampler = lambda: 0
        elif big_mag:
            byte_size = int(math.ceil(math.log(mag, 2) / 8))
            sampler = lambda: int.from_bytes(self.randbytes(byte_size), byteorder='big')
        else:
            sampler = lambda: self.gen.integers(0, mag, endpoint=True)

        for _ in range(size or 1):
            while True:  # rejection sampling
                guess = int(low + sampler())
                if guess <= high:
                    break

            if single:
                return guess
            else:
                res.append(guess)
        return res

    def randint_inversion(self, low, high, size=None):
        """Does not work well if high >= 2**53 due to float precision"""
        mag = high - low
        res = []
        single = size is None

        if not self.warned_high_inv and mag >= self.DOUBLE_LIMIT:
            self.warned_high_inv = True
            logger.warning('Magnitude is higher than 2**53, results can be invalid or imprecise')

        unifs = self.uniform(0, 1, size) if mag < self.DOUBLE_LIMIT else self.random_precise(math.log(mag, 2))
        for i in range(size or 1):
            uu = unifs if single else unifs[i]
            guess = int(mag * uu) + low
            if single:
                return guess
            else:
                res.append(guess)
        return res

    def randbytes(self, length):
        return self.gen.bytes(length)

    def randbits(self, bits):
        return self.randint(0, (2 << bits)-1)

    def uniform(self, low, high, size=None):
        if not self.warned_high_uni and high >= self.INT64_LIMIT:
            self.warned_high_uni = True
            logger.warning('High is higher than INT64, results can be invalid or imprecise')

        return self.gen.uniform(low, high, size=size)

    def random(self, size=None):
        return self.gen.random(size)

    def normal(self, loc=0.0, scale=1.0, size=None):
        return self.gen.normal(loc=loc, scale=scale, size=size)


def rand_moduli(mod, gen: RGenerator):
    while True:
        yield from gen.randint(0, mod - 1, 2048)


def rand_gen_randint(low, high, gen: RGenerator, chunk=2048):
    while True:
        yield from gen.randint(low, high, chunk)


def rand_gen_uniform(low, high, gen: RGenerator, chunk=2048):
    while True:
        yield from gen.uniform(low, high, chunk)


def rand_gen_uniform_prec(low, high, gen: RGenerator, chunk=2048, precision=50):
    while True:
        yield from gen.uniform_precise(low, high, chunk, precision)


def rand_moduli_bias_frac(mod, gen: Optional[RGenerator], p=0.001, frac=10):
    gen_p = rand_gen_uniform(0, 1, gen)
    gen_uni = rand_gen_randint(0, mod - 1, gen)
    gen_bias = rand_gen_randint(int(mod/frac), int(mod*(frac-1)/frac), gen)  # 1/10 ... 9/10 of the mod
    while True:
        cp = next(gen_p)
        if cp <= p:
            yield next(gen_bias)
        else:
            yield next(gen_uni)


def rand_gen_mod_normal(mod, gen: RGenerator, loc=None, scale=None, chunk=2048):
    while True:
        for x in gen.normal(loc or 0.0, scale or 1.0, chunk):
            cx = int(x * (mod//4) + (mod//2))
            if cx < 0 or cx >= mod:
                continue
            yield cx


def rand_gen_alpha(st, gen: RGenerator, mod=None, omax=None, chunk=2048):
    while True:
        sgen = None  # 1=osize, 2=mod, 3=normal
        if st == 1:
            sgen = rand_gen_randint(0, omax - 1, gen, chunk=chunk)
        elif st == 2:
            sgen = rand_gen_randint(0, mod - 1, gen, chunk=chunk)
        elif st == 3:
            sgen = rand_gen_mod_normal(mod, gen, chunk=chunk)
        else:
            raise ValueError('Unknown st: %s' % (st,))

        for x in sgen:
            cx = pow(x, 3, mod)
            yield cx


class ModSpreader:
    """
    Takes a number from Z_m and with auxiliar randomness coin flips distributes it to N bits uniformly.

    If input distribution over Z_m is uniform, resulting distribution over 2**N should be uniform as well.
    Alternatively, the bias in th input distribution should be present also in the stretched distribution.

    Strategies that work well: 7, 6, 10. Rejection sampling / inversion sampling.
    """
    def __init__(self, m=None, osize=None, gen: Optional[RGenerator] = None):
        self.m = m
        self.osize = osize
        self.gen = gen

        self.max = (2 ** osize)
        self.max_mask = self.max - 1
        self.tp = self.max // m  # number of full-sized ms inside the range
        self.tc = math.ceil(self.max / self.m) - 1  # number of full-sized ms inside the range
        self.bp = self.max / m   # precise fraction
        self.rm = self.max - self.tp * self.m
        self.msize = int(log2ceil(m))
        self.mmin1_frac = fractions.Fraction(1, self.m - 1)

        self.gen_randint_0_tp = rand_gen_randint(0, max(0, self.tc), gen)
        self.gen_randint_0_maxm1 = rand_gen_randint(0, self.max - 1, gen)
        self.gen_uniform_0_bp = rand_gen_uniform(0, self.bp, gen)
        self.gen_uniform_0_step = rand_gen_uniform(0, max(0, 1 / (self.m - 1.0)), gen)
        self.gen_uniform_0_step_frac = rand_gen_uniform_prec(0, self.mmin1_frac, gen,
                                                             precision=max(osize, math.log(m if m >= 1 else 2, 2)))

        self.m_bits = int(math.log(m, 2)) if m > 1 else 0
        self.mask_size = max(0, osize - self.m_bits)
        self.gen_randint_mask = rand_gen_randint(0, 2**self.mask_size - 1, gen) if self.mask_size else None

        if self.max < self.m:
            logger.warning("Moduli is greater than maximum, some strategies might not work")
        if max(self.max_mask, self.m - 1) >= 2**63:
            logger.info("Working with numbers >= INT64.MAX, some strategies won't work (e.g., inversion sampling)")

        if self.max >= self.m:
            # Rejection ratio: prob of highest m-offset * portion of overflowing chunk out of m
            rej_ratio = 1 / (self.tc + 1) * ((self.tc + 1) * self.m - self.max) / self.m
            logger.info("Expected rejection ratio: %s" % (rej_ratio,))

        elif self.max < self.m:
            # Masking bias: full m inside max gives 1 weight to max interval values.
            # If x*m is on boundary of max, lower values give 1 weight more than values above m
            mask_bias_0 = self.m % self.max
            mask_bias_m = min(mask_bias_0, self.max - mask_bias_0)
            mask_bias_r = mask_bias_m / self.max_mask
            mask_bias_w = self.m // self.max  # how many full-widths, base. Bias is then mask_bias_w+1 / mask_bias_w
            mask_bias_ws = '%s:%s' % ((mask_bias_w, mask_bias_w + 1) if mask_bias_0 == mask_bias_m
                                      else (mask_bias_w + 1, mask_bias_w))
            rejection_drop = self.max / self.m
            logger.info("Expected masking bias on range %s (%s values), weight %s. Accept rate for drop above max: %s"
                        % (mask_bias_r, mask_bias_m, mask_bias_ws, rejection_drop))

    def spread(self, z):
        """1: Spread number z inside range (0 ... m) to osize, biases in one end"""
        z %= self.m
        return (self.m * self.gen.randint(0, self.tp if z < self.rm else self.tp - 1)) + z

    def spread_weak(self, z):
        """2: Spreads number inside range (0 ... m) to osize, with bias on lower moduli range"""
        z %= self.m
        return z + (self.gen.randbits(self.osize - self.msize) << self.msize)

    def spread_weak_minus(self, z):
        """3: Spreads number inside range (0 ... m) to osize, with bias - upper moduli is not covered"""
        z %= self.m
        y = self.gen.randbits(self.osize)
        return (y - (y % self.m)) + z

    def spread_weak_weird(self, z):
        """4: For testing, generates highly non-uniform distribution (resembles a company logo)"""
        z %= self.m
        y = self.gen.randbits(self.osize)
        return (y - self.m if y >= self.m else y) + z

    def spread_flat(self, z):
        """5: For testing, introducing significant bias by masking random positions in moduli to zero"""
        p = self.gen.randbits(self.gen.randint(0, 8))
        z &= ~p
        return self.spread(z)

    def spread_reject(self, z):
        """6: Rejection sampling, smaller data size, works!
        Idea: generate random m-offset, add z to the offset. If goes above the limit, reject the sample.
        Any other attempt to deal with overflows usually ends in skewing the distribution.
        """
        x = (self.m * next(self.gen_randint_0_tp)) + z
        return x if x < self.max else None

    def spread_gen(self, z):
        """7: Rejection sampling, with aux gen, works also!
        Idea: similar to spread_reject, instead of rejecting the sample we generate uniform number from aux generator.
        Useful for preserving data size"""
        x = (self.m * next(self.gen_randint_0_tp)) + z
        return x if x < self.max else next(self.gen_randint_0_maxm1)

    def spread_wider(self, z):
        """8: Cannot detect biases, z is basically ignored"""
        z %= self.m
        return int(next(self.gen_uniform_0_bp) * self.m + z) & self.max_mask

    def spread_wider_reject(self, z):
        """9: Cannot detect biases, z is basically ignored"""
        z %= self.m
        x = int(next(self.gen_uniform_0_bp) * self.m + z)
        return x if x < self.max else None

    def spread_inverse_sample(self, z):
        """10: Inversion sampling, https://en.wikipedia.org/wiki/Inverse_transform_sampling
        Intuition: use z to cover the whole interval. Without correction, there would be gaps (e.g., hit only each 4th
          number). Use then U() generator to cover the holes. Minimum rejections.
        Warning: due to float multiplication, this method works only for sizes up 2**53
        https://docs.python.org/3/tutorial/floatingpoint.html IEEE-754

          - z is in the interval [0, m-1], uniform. Then Y = z/(m-1) is on [0, 1]
          - step = 1/(m-1) is a difference of two closest values from Y distribution, numbers "inside" the step
            are not present.  |-----|-----|------|  (gap ----- is not covered by Y, just | are covered)
          - to expand the range of a function, generate sub-step precision with an uniform distribution
            (to spread outcomes across the step window)
          - Resulting distribution expanded on the whole interval: Y + U(0, step) =
            (z / (m-1)) + U(0, 1/(m-1)), note U interval is open on the upper end. This is OK, not to hit next box.
          - Rejections: minimal, only if the z == m-1, we are hitting few numbers above the interval.
            Those are rejected.
          - Potential problem: if z == m-1 is biased, the chance of discovering this is a bit lower than other numbers.
            Due to spread to higher numbers, it is spread across mx / (m-1), thus prob. is (m-1) / mx
        """
        z %= self.m
        u = (z / (self.m - 1.0))  # uniform dist on [0, 1], step is 1/(m-1)
        x = int((u + next(self.gen_uniform_0_step)) * self.max_mask)
        return x if x < self.max else None

    def spread_rand(self, z):
        """11: Completely random, ignoring input"""
        x = int(next(self.gen_randint_0_maxm1))
        return x if x < self.max else None

    def spread_mask_fixed(self, z):
        """12: always enable 15th bit, bias"""
        z %= self.m
        return z | (1 << 15)

    def spread_mask(self, z):
        """13: Masking with osize. If 2**osize / m is not an integer, it is biased"""
        z %= self.m
        return z & self.max_mask

    def spread_inverse_gaps(self, z):
        """14: 2**osize % mod number of gaps"""
        z %= self.m
        x = (z << self.osize) // self.m  # u = z * (2**osize) / m, avoiding floating division
        return x if x < self.max else None

    def spread_inverse_frac(self, z):
        """15: Uses unlimited precision uniform number generator and fractions to compute inverse"""
        u = (z % self.m) * self.mmin1_frac  # uniform dist on [0, 1], step is 1/(m-1)
        x = int((u + next(self.gen_uniform_0_step_frac)) * self.max_mask)
        return x if x < self.max else None

    def spread_drop(self, z):
        """16: if max < modulus, just drop everything above max. Same as spread_reject, but faster"""
        return z if z < self.max else None

    def spread_drop_gen(self, z):
        """17: if max < modulus, use z if < max, else generate a random integer. Same as spread_gen, but faster"""
        return z if z < self.max else next(self.gen_randint_0_maxm1)

    def spread_expand(self, z):
        """18: For mod < max, bit-aligned mod. Generate upper mask randomly"""
        r = next(self.gen_randint_mask)
        z |= r << self.m_bits
        return z if z < self.max else None

    def spread_inverse_large(self, z):
        """NA: Attempt to do spread_inverse_frac with large number operation, faster. Not finished."""
        z %= self.m
        u = (z << self.osize) // self.m  # u = z * (2**osize) / m, avoiding floating division
        # step = 259 is step for 2**16 vs 0xff03 = 1/((2**16 / 0xff03) - 1)

        # Number of missing elements = 65536 % modulus = 253
        # Additive step: 65536 / (65536 % 0xff03) = 259.0355731225296
        #  ==> 1 / 0.0355731225296 = 28.111111111146094 -> each 28th new overflow (259.0355731225296 * 27, * 28, * 29)

        # aa = [((i) << 16) // 0xff3d for i in range(0xff3d)]; aas=set(aa)
        # bb=[x for x in range(2**16) if x not in aas]
        # [bb[i]-bb[i+1] for i in range(len(bb)-1)]
        # [(i,x) for i,x in enumerate(bbb) if x != -259]

        # more precise method: gen 50-bit precision uniform, delete by 1/50 in fraction()
        # or decimal.getcontext().prec = 800
        x = int((u + next(self.gen_uniform_0_step)) * self.max_mask)
        return x if x < self.max else None


class DataGenerator:
    def __init__(self):
        self.args = None
        self.rng = None

    def main(self):
        parser = self.argparser()
        self.args = parser.parse_args()

        if self.args.debug:
            coloredlogs.install(level=logging.DEBUG)

        self.work()

    def work(self):
        seed = binascii.unhexlify(self.args.seed) if self.args.seed else None
        if self.args.rgen in ['pcg', 'pcg32', 'pcg64', 'numpy', 'np']:
            self.rng = RGeneratorPCG(seed)
        elif self.args.rgen in ['aes'] or self.args.rgen is None:
            self.rng = RGeneratorPCG(seed, cls=AESCounter, cls_kw={'mode': 'sequence'})
        elif self.args.rgen in ['chacha'] or self.args.rgen is None:
            self.rng = RGeneratorPCG(seed, cls=ChaCha, cls_kw={'mode': 'sequence'})
        elif self.args.rgen in ['sys', 'py', 'random'] or self.args.rgen is None:
            self.rng = RGeneratorRandom(seed)
        else:
            raise ValueError('Unknown generator: %s' % (self.args.rgen, ))

        is_binary = self.args.binary or self.args.binary_randomize
        is_binary_rand = self.args.binary_randomize
        mod = int(self.args.mod, 16) if self.args.mod else None
        mod_size = int(log2ceil(mod)) if mod else None

        osize = self.args.osize
        isize = self.args.isize
        if not isize and mod:
            isize = mod_size
        if not mod_size and isize:
            mod_size = isize
        if not osize and isize:
            osize = isize
        if not osize and mod_size:
            osize = mod_size

        osize_b = int(math.ceil(osize / 8.))
        isize_b = int(math.ceil(isize / 8.))
        osize_baligned = osize_b * 8 == osize
        isize_baligned = isize_b * 8 == isize

        read_multiplier = 8 / gcd(isize, 8)
        read_chunk_base = int(isize * read_multiplier)
        read_chunk = read_chunk_base * max(1, 65_536 // read_chunk_base)  # expand a bit
        max_len = self.args.max_len
        max_out = self.args.max_out
        cur_len = 0
        cur_out = 0
        n_elems_read = 0

        spreader = ModSpreader(m=mod, osize=osize, gen=self.rng) if mod else None
        spread_func = lambda x: x  # identity by default
        output_fh = sys.stdout.buffer if not self.args.ofile else open(self.args.ofile, 'w+b')
        oseq = OutputSequencer(ostream=output_fh, fsize=osize, osize=osize, endian=self.args.output_endian,
                               use_bit_precision=is_binary or self.args.binary_precision,
                               hexlify=self.args.ohex)

        if spreader:
            st = self.args.strategy
            if st == 0:
                logger.info('Strategy: identity')
            elif st == 1:
                spread_func = spreader.spread
                logger.info('Strategy: spread (biased)')
            elif st == 2:
                spread_func = spreader.spread_weak
                logger.info('Strategy: spread_weak (biased, strong)')
            elif st == 3:
                spread_func = spreader.spread_weak_minus
                logger.info('Strategy: spread_weak_minus (biased, strong)')
            elif st == 4:
                spread_func = spreader.spread_weak_weird
                logger.info('Strategy: spread_weak_weird (biased, strong)')
            elif st == 5:
                spread_func = spreader.spread_flat
                logger.info('Strategy: spread_weak_weird (biased, significant)')
            elif st == 6:
                spread_func = spreader.spread_reject
                logger.info('Strategy: spread_reject (rejection sampling, unbiased, drops values out of range)')
            elif st == 7:
                spread_func = spreader.spread_gen
                logger.info('Strategy: spread_reject (rejection sampling, unbiased, '
                            'generates uniform values for drops)')
            elif st == 8:
                spread_func = spreader.spread_wider
                logger.info('Strategy: spread_wider (drops input (xor), biased for large osize or mod)')
            elif st == 9:
                spread_func = spreader.spread_wider_reject
                logger.info('Strategy: spread_wider_reject (drops input (xor), biased for large osize or mod)')
            elif st == 10:
                spread_func = spreader.spread_inverse_sample
                logger.info('Strategy: inversion sampling (works on limited range)')
                if max(spreader.m, spreader.max_mask) >= 2**50:  # https://docs.python.org/3/tutorial/floatingpoint.html
                    logger.warning('Inversion sampling does not work for large numbers (float precision)')
            elif st == 11:
                spread_func = spreader.spread_rand
                logger.info('Strategy: spread_rand (uniform, ignores input)')
            elif st == 12:
                spread_func = spreader.spread_mask_fixed
                logger.info('Strategy: spread_mask_fixed (input & mask, biased 15th bit)')
            elif st == 13:
                spread_func = spreader.spread_mask
                logger.info('Strategy: spread_mask (slight bias, '
                            'masks input with osize maks, works only for 2*mod >= 2**osize)')
                if 2*spreader.m < spreader.max_mask:
                    logger.warning('Masking strategy is highly biased with 2*mod < 2**osize')
            elif st == 14:
                spread_func = spreader.spread_inverse_gaps
                logger.info('Strategy: spread_inverse_gaps (simple spread with gaps, has bias)')
            elif st == 15:
                spread_func = spreader.spread_inverse_frac
                logger.info('Strategy: spread_inverse_frac (inversion sampling with unlimited precision)')
            elif st == 16:
                spread_func = spreader.spread_drop
                logger.info('Strategy: spread_drop')
            elif st == 17:
                spread_func = spreader.spread_drop_gen
                logger.info('Strategy: spread_drop_gen')
            elif st == 18:
                spread_func = spreader.spread_expand
                logger.info('Strategy: spread_expand')
            else:
                raise ValueError('No such strategy')

        gen_ctr = counter(self.args.inp_ctr_off, mod) if self.args.inp_ctr else None
        gen_moduli = rand_moduli(mod, self.rng) if self.args.rand_mod else None
        sha256_read = hashlib.sha256()
        sha256_proc = hashlib.sha256()
        nbyte_read = 0
        nbyte_proc = 0

        b = bitarray(endian=self.args.input_endian)
        b_filler = bitarray(isize_b * 8 - isize, endian=self.args.input_endian)
        b_filler.setall(0)
        b_pad = None
        b_pad_rand = None
        b_pad_rand_size = max(8, 8 * int(math.ceil((osize - isize) / 8.)))
        if is_binary and osize > isize:
            b_pad = bitarray(osize - isize, endian=self.args.output_endian)
            b_pad.setall(0)
            b_pad_rand = bitarray(b_pad_rand_size, endian=self.args.output_endian)
            b_pad_rand.setall(0)

        osize_mask = (2 ** (osize_b * 8)) - 1
        nrejects = 0
        noverflows = 0
        time_start = time.time()
        logger.info("Generating data")
        fh = open(self.args.file, 'rb+') if self.args.file else None

        while True:
            if self.args.stdin:
                data = sys.stdin.buffer.read(read_chunk)
            elif fh is not None:
                data = fh.read(read_chunk)
            elif gen_ctr:
                data = number_streamer(gen_ctr, isize, read_chunk, endian=self.args.input_endian)
            elif gen_moduli:
                data = number_streamer(gen_moduli, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias1:
                gg = rand_moduli_bias_frac(mod, self.rng, 0.0001, 10)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias2:
                gg = rand_moduli_bias_frac(mod, self.rng, 0.01, 7)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias3:
                gg = rand_moduli_bias_frac(mod, self.rng, 0.01, 4)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias4:
                gg = rand_moduli_bias_frac(mod, self.rng, 0.1, 3)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias5:
                gg = rand_gen_mod_normal(mod, self.rng)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            elif self.args.rand_mod_bias6 != 0:
                gg = rand_gen_alpha(self.args.rand_mod_bias6, self.rng, mod=mod, omax=2**osize)
                data = number_streamer(gg, isize, read_chunk, endian=self.args.input_endian)
            else:
                data = self.rng.randbytes(read_chunk)

            if not data:
                break

            sha256_read.update(data)
            nbyte_read += len(data)

            # Manage output size constrain in bits
            cblen = len(data) * 8
            last_chunk_sure = False
            if max_len is not None and cur_len + cblen > max_len:
                rest = max_len - cur_len
                data = data[:rest//8]
                cblen = rest
                last_chunk_sure = True

            cur_len += cblen
            elems = cblen // isize
            sha256_proc.update(data)
            nbyte_proc += len(data)

            if cblen % isize != 0 and not last_chunk_sure:
                logger.warning('Read bits not aligned, %s vs isize %s, mod: %s. May happen for the last chunk.'
                               % (cblen, isize, cblen % isize))

            b.clear()
            b.frombytes(data)

            # Parse on ints
            for i in range(elems):
                n_elems_read += 1
                cbits = b[i * isize: (i+1) * isize]

                if is_binary:
                    # Binary field, covers full bit-width
                    if isize == osize:
                        oseq.dump_bits(cbits)

                    elif isize < osize:  # pad with zeros or random bits
                        if is_binary_rand:
                            rnd_data = self.rng.randbytes(b_pad_rand_size / 8)
                            b_pad_rand.clear()
                            b_pad_rand.frombytes(rnd_data)
                            b_pad = b_pad_rand[:osize - isize]
                        oseq.dump_bits(b_pad + cbits)

                    else:  # isize > osize, truncate, take right-most (big-endian encoding -> least significant bits)
                        oseq.dump_bits(cbits[-(isize - osize):])

                else:
                    # F_n, Z_n
                    cbits = b_filler + cbits
                    cbytes = cbits.tobytes()
                    celem = int.from_bytes(bytes=cbytes, byteorder=self.args.input_endian)
                    spreaded = spread_func(celem)
                    if spreaded is None:
                        nrejects += 1
                        continue
                    if spreaded > osize_mask:
                        noverflows += 1

                    oelem = int(spreaded) & osize_mask
                    oseq.dump_int(oelem)

                cur_out += osize
                if max_out is not None and cur_out >= max_out:
                    break

            finishing = data is None \
                        or (max_len is not None and max_len <= cur_len) \
                        or (max_out is not None and max_out <= cur_out)
            oseq.maybe_flush(finishing)

            if finishing:
                oseq.flush()
                output_fh.flush()
                break

        time_elapsed = time.time() - time_start
        hash_read = sha256_read.hexdigest()
        hash_proc = sha256_read.hexdigest()
        hash_written = oseq.sha256_written.hexdigest()
        logger.info("Processing finished")
        logger.info("%s B read, SHA256 read: %s" % (nbyte_read, hash_read))

        if hash_read != hash_proc:
            logger.info("%s B proc, SHA256 proc: %s" % (nbyte_proc, hash_proc))

        logger.info("%s B written, SHA256 written: %s" % (oseq.bits_written // 8, hash_written))
        logger.info("Number of rejects: %s, overflows: %s, elems: %s, time: %s s"
                    % (nrejects, noverflows, n_elems_read, time_elapsed, ))
        if self.args.ofile:
            output_fh.close()

    def argparser(self):
        parser = argparse.ArgumentParser(description='Data spreader - for moduli functions')

        parser.add_argument('--debug', dest='debug', action='store_const', const=True,
                            help='enables debug mode')
        parser.add_argument('-i', '--stdin', dest='stdin', action='store_const', const=True,
                            help='Read input stdin')
        parser.add_argument('-f', '--file', dest='file',
                            help='Input file to read')
        parser.add_argument('-r', '--rand', dest='rand', action='store_const', const=True,
                            help='Generate randomness internally')
        parser.add_argument('--rgen', dest='rgen', default='aes',
                            help='Random number generator implementation (aes)')
        parser.add_argument('--inp-rand-mod', dest='rand_mod', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range')
        parser.add_argument('--inp-rand-mod-bias1', dest='rand_mod_bias1', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias1')
        parser.add_argument('--inp-rand-mod-bias2', dest='rand_mod_bias2', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias2')
        parser.add_argument('--inp-rand-mod-bias3', dest='rand_mod_bias3', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias3')
        parser.add_argument('--inp-rand-mod-bias4', dest='rand_mod_bias4', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias4')
        parser.add_argument('--inp-rand-mod-bias5', dest='rand_mod_bias5', action='store_const', const=True,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias5 - normal')
        parser.add_argument('--inp-rand-mod-bias6', dest='rand_mod_bias6', type=int,
                            help='Input method: Generate randomness internally, generating random integer in mod range,'
                                 ' bias6 - ^3. 1=osize, 2=mod, 3=normal')
        parser.add_argument('--inp-ctr', dest='inp_ctr', action='store_const', const=True,
                            help='Input method: Input counter generator')
        parser.add_argument('--inp-ctr-off', dest='inp_ctr_off', type=int, default=0,
                            help='Input counter generator offset')
        parser.add_argument('-b', '--binary', dest='binary', action='store_const', const=True,
                            help='Input is binary field, no moduli')
        parser.add_argument('--br', '--binary-randomize', dest='binary_randomize', action='store_const', const=True,
                            help='Input is binary field, no moduli, randomize padded values')
        parser.add_argument('--bp', '--binary-precision', dest='binary_precision', action='store_const', const=True,
                            help='Force binary precision, always use bitarrays')
        parser.add_argument('--ie', '--input-endian', dest='input_endian', default='big',
                            help='Input endianness')
        parser.add_argument('--oe', '--output-endian', dest='output_endian', default='big',
                            help='Input endianness')
        parser.add_argument('-s', '--seed', dest='seed',
                            help='Seed for random generator')
        parser.add_argument('-m', '--mod', dest='mod',
                            help='Hex-coded modulus to spread')
        parser.add_argument('--ib', dest='isize', type=int,
                            help='Input block size in bits (when using on stdin)')
        parser.add_argument('--ob', dest='osize', type=int,
                            help='Output block size in bits (to spread)')
        parser.add_argument('--st', dest='strategy', type=int, default=0,
                            help='Strategy to use for spreading')
        parser.add_argument('--max-len', dest='max_len', type=int,
                            help='Maximum length in bits when working with generator')
        parser.add_argument('--max-out', dest='max_out', type=int,
                            help='Maximum length in bits for output')
        parser.add_argument('--ohex', dest='ohex', action='store_const', const=True,
                            help='Output hex-coded')
        parser.add_argument('--ofile', dest='ofile',
                            help='Dump to output file')
        return parser


def main():
    br = DataGenerator()
    return br.main()


if __name__ == '__main__':
    main()
