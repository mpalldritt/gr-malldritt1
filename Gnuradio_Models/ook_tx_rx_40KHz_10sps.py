#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ook_tx_rx_40KHz_10sps
# Author: MA & RB
# Description: Simulator for testing multipath
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from mp_channel_complex import mp_channel_complex  # grc-generated hier_block
import sip



class ook_tx_rx_40KHz_10sps(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ook_tx_rx_40KHz_10sps", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ook_tx_rx_40KHz_10sps")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ook_tx_rx_40KHz_10sps")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 10
        self.samp_rate = samp_rate = 100000
        self.num_syms = num_syms = 1000
        self.noise_level = noise_level = 20
        self.delay = delay = 2900
        self.center_freq = center_freq = 40e3

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            100, #size
            int(symbol_rate), #samp_rate
            "Errors", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-0.1, 1.1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.5, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Errors', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [0, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            (int(samp_rate/symbol_rate)*50), #size
            samp_rate, #samp_rate
            "Signals (TX and RX)", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-0.1, 1.1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(False)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)


        labels = ['TX Signal', 'RX Signal', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("SNR in dB")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.mp_channel_complex_0 = mp_channel_complex(
            air_gain=0,
            air_velocity=340,
            path_length=1,
            samp_rate=samp_rate,
            steel_gain=0.8,
            steel_velocity=5000,
            wood_gain=0.2,
            wood_velocity=3000,
        )
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate,
                (4*symbol_rate),
                (10*symbol_rate),
                window.WIN_HAMMING,
                6.76))
        self.blocks_xor_xx_0 = blocks.xor_bb()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_threshold_ff_3 = blocks.threshold_ff(0.2, 0.8, 0)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_int*1, (int(samp_rate/symbol_rate)))
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(20, 1, 0)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_keep_one_in_n_0_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, (int(samp_rate/symbol_rate)))
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, (int(samp_rate/symbol_rate)))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/home/michael/Desktop/Combined desktop folders MA22082025/Gnuradio_Models/ch5/BER-test-data.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_divide_xx_0_0 = blocks.divide_ff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.band_pass_filter_1 = filter.fir_filter_fcc(
            1,
            firdes.complex_band_pass(
                2,
                samp_rate,
                (center_freq - 5*symbol_rate),
                (center_freq + 5*symbol_rate),
                (10*symbol_rate),
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, center_freq, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, num_syms))), False)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_level, 0)
        self.analog_const_source_x_1_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, noise_level)
        self.analog_const_source_x_1_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_1_0_0, 0), (self.blocks_divide_xx_0_0, 0))
        self.connect((self.analog_const_source_x_1_1, 0), (self.blocks_divide_xx_0_0, 1))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_1, 0), (self.mp_channel_complex_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_divide_xx_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_xor_xx_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.blocks_xor_xx_0, 1))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_threshold_ff_3, 0), (self.blocks_keep_one_in_n_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_3, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_xor_xx_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_threshold_ff_3, 0))
        self.connect((self.mp_channel_complex_0, 0), (self.blocks_complex_to_mag_squared_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ook_tx_rx_40KHz_10sps")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.band_pass_filter_1.set_taps(firdes.complex_band_pass(2, self.samp_rate, (self.center_freq - 5*self.symbol_rate), (self.center_freq + 5*self.symbol_rate), (10*self.symbol_rate), window.WIN_HAMMING, 6.76))
        self.blocks_keep_one_in_n_0_0.set_n((int(self.samp_rate/self.symbol_rate)))
        self.blocks_keep_one_in_n_0_0_0.set_n((int(self.samp_rate/self.symbol_rate)))
        self.blocks_repeat_0.set_interpolation((int(self.samp_rate/self.symbol_rate)))
        self.low_pass_filter_1.set_taps(firdes.low_pass(2, self.samp_rate, (4*self.symbol_rate), (10*self.symbol_rate), window.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_2.set_samp_rate(int(self.symbol_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_1.set_taps(firdes.complex_band_pass(2, self.samp_rate, (self.center_freq - 5*self.symbol_rate), (self.center_freq + 5*self.symbol_rate), (10*self.symbol_rate), window.WIN_HAMMING, 6.76))
        self.blocks_keep_one_in_n_0_0.set_n((int(self.samp_rate/self.symbol_rate)))
        self.blocks_keep_one_in_n_0_0_0.set_n((int(self.samp_rate/self.symbol_rate)))
        self.blocks_repeat_0.set_interpolation((int(self.samp_rate/self.symbol_rate)))
        self.low_pass_filter_1.set_taps(firdes.low_pass(2, self.samp_rate, (4*self.symbol_rate), (10*self.symbol_rate), window.WIN_HAMMING, 6.76))
        self.mp_channel_complex_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_num_syms(self):
        return self.num_syms

    def set_num_syms(self, num_syms):
        self.num_syms = num_syms

    def get_noise_level(self):
        return self.noise_level

    def set_noise_level(self, noise_level):
        self.noise_level = noise_level
        self.analog_const_source_x_1_1.set_offset(self.noise_level)
        self.analog_noise_source_x_0_0.set_amplitude(self.noise_level)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(self.delay))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.analog_sig_source_x_1.set_frequency(self.center_freq)
        self.band_pass_filter_1.set_taps(firdes.complex_band_pass(2, self.samp_rate, (self.center_freq - 5*self.symbol_rate), (self.center_freq + 5*self.symbol_rate), (10*self.symbol_rate), window.WIN_HAMMING, 6.76))




def main(top_block_cls=ook_tx_rx_40KHz_10sps, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start(1000)

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
