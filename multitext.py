#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='generate multitext files.')
parser.add_argument('-F', '--file', action='store', type=argparse.FileType('w', encoding='ascii'), 
                    dest='filename', 
                    help='output to FILE (or stdout if not specified)', 
                    metavar='FILE')
parser.add_argument('-p', '--prefix', action='store', type=str, dest='prefix', 
                    help='text string to prepend to each line of output', 
                    default='', metavar='STRING')
parser.add_argument('-s', '--suffix', action='store', type=str, dest='suffix', 
                    help='text string to append to each line of output', 
                    default='', metavar='STRING')
parser.add_argument('-f', '--float', action='store', type=int, dest='fpoints', 
                    help='number of floating points to output in text format',
                    default=2, metavar='NUM')
parser.add_argument('-i', '--int', '--integer', action='store_true', dest='integer', 
                    help='only output whole numbers (integers)')
parser.add_argument('--sci', action='store_true', dest='sci', 
                    help='use sci unit scales (u,m,K,M,etc)')
parser.add_argument('-r', '--ratio', action='store_true', dest='ratio', 
                    help='output number as a ratio')
parser.add_argument('-k', '--keys', '--midi', action='store_true', dest='midi', 
                    help='convert values to MIDI notes (works best with integer steps)')
parser.add_argument('--sharps', action='store_true', dest='sharps', 
                    help='represent MIDI note numbers (-k option) as sharps instead of flats')
parser.add_argument('start', action='store', type=int, 
                    help='number to start on')
parser.add_argument('step', action='store', type=float, 
                    help='step size')
parser.add_argument('end', action='store', type=int, 
                    help='number to end on')

args = parser.parse_args()

if args.sharps:
    midi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
else:
    midi = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

if args.integer:
    format_num = '%.0f'
else:
    format_num = ''.join(['%.', "%i" % (args.fpoints), 'f'])

for i in range(0, int((args.end - args.start) * (1.0 / args.step)) + 1):
    absval = (i * args.step) + args.start
    num = format_num % (absval)
    if args.midi:
        print("%s%s%i%s" % (args.prefix, midi[int(absval % 12)], int(absval / 12), args.suffix))
    elif args.ratio:
        num2 = format_num % (args.end - absval)
        print('%s%s:%s%s' % (args.prefix, num, num2, args.suffix))
    else:
        print('%s%s%s' % (args.prefix, num, args.suffix))
