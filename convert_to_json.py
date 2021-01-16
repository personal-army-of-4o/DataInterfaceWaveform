from vcd2json.vcd2json import WaveExtractor
import sys

name = sys.argv[1]
extractor = WaveExtractor(name + '.vcd', name + '.json', ['uut/iclk', 'uut/ivalid', 'uut/idata[7:0]', 'uut/oack'])
extractor.wave_chunk=0
extractor.execute()
