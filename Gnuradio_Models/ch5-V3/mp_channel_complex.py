# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MP Channel hier block
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class mp_channel_complex(gr.hier_block2):
    def __init__(self, air_gain=0, air_velocity=340, path_length=1, samp_rate=0, steel_gain=0, steel_velocity=5000, wood_gain=0, wood_velocity=3000):
        gr.hier_block2.__init__(
            self, "MP Channel hier block",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.air_gain = air_gain
        self.air_velocity = air_velocity
        self.path_length = path_length
        self.samp_rate = samp_rate
        self.steel_gain = steel_gain
        self.steel_velocity = steel_velocity
        self.wood_gain = wood_gain
        self.wood_velocity = wood_velocity

        ##################################################
        # Blocks
        ##################################################
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_cc(steel_gain)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(wood_gain)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(air_gain)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*1, int(path_length/steel_velocity*samp_rate))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, int(path_length/wood_velocity*samp_rate))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(path_length/air_velocity*samp_rate))
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.blocks_delay_0_0, 0))
        self.connect((self, 0), (self.blocks_delay_0_1, 0))


    def get_air_gain(self):
        return self.air_gain

    def set_air_gain(self, air_gain):
        self.air_gain = air_gain
        self.blocks_multiply_const_vxx_0.set_k(self.air_gain)

    def get_air_velocity(self):
        return self.air_velocity

    def set_air_velocity(self, air_velocity):
        self.air_velocity = air_velocity
        self.blocks_delay_0.set_dly(int(self.path_length/self.air_velocity*self.samp_rate))

    def get_path_length(self):
        return self.path_length

    def set_path_length(self, path_length):
        self.path_length = path_length
        self.blocks_delay_0.set_dly(int(self.path_length/self.air_velocity*self.samp_rate))
        self.blocks_delay_0_0.set_dly(int(self.path_length/self.wood_velocity*self.samp_rate))
        self.blocks_delay_0_1.set_dly(int(self.path_length/self.steel_velocity*self.samp_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_delay_0.set_dly(int(self.path_length/self.air_velocity*self.samp_rate))
        self.blocks_delay_0_0.set_dly(int(self.path_length/self.wood_velocity*self.samp_rate))
        self.blocks_delay_0_1.set_dly(int(self.path_length/self.steel_velocity*self.samp_rate))

    def get_steel_gain(self):
        return self.steel_gain

    def set_steel_gain(self, steel_gain):
        self.steel_gain = steel_gain
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.steel_gain)

    def get_steel_velocity(self):
        return self.steel_velocity

    def set_steel_velocity(self, steel_velocity):
        self.steel_velocity = steel_velocity
        self.blocks_delay_0_1.set_dly(int(self.path_length/self.steel_velocity*self.samp_rate))

    def get_wood_gain(self):
        return self.wood_gain

    def set_wood_gain(self, wood_gain):
        self.wood_gain = wood_gain
        self.blocks_multiply_const_vxx_0_0.set_k(self.wood_gain)

    def get_wood_velocity(self):
        return self.wood_velocity

    def set_wood_velocity(self, wood_velocity):
        self.wood_velocity = wood_velocity
        self.blocks_delay_0_0.set_dly(int(self.path_length/self.wood_velocity*self.samp_rate))

