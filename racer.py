import argparse
from commands.subcommand import command_train, command_demo

parser = argparse.ArgumentParser(description='Learning Racer command.')
subparser = parser.add_subparsers()

# train subcommand.
parser_train = subparser.add_parser('train', help='see `train -h`')
parser_train.add_argument('-vae', '--vae-path', help='Path to a trained vae model path.',
                    default='vae.torch', type=str)
parser_train.add_argument('-device', '--device', help='torch device {"cpu" | "cuda"}',
                    default='cuda', type=str)
parser_train.add_argument('-robot', '--robot-driver', help='choose robot driver',
                    default='jetbot', type=str)
parser_train.add_argument('-steps', '--time-steps', help='total step.',
                    default='5000', type=int)
parser_train.add_argument('-s', '--save', help='save model file name.',
                    default='model', type=str)
parser_train.set_defaults(handler=command_train)

# demo subcommand.
parser_demo = subparser.add_parser('demo', help='see `demo -h`')
parser_demo.add_argument('-vae', '--vae-path', help='Path to a trained vae model path.',
                    default='vae.torch', type=str)
parser_demo.add_argument('-model', '--model-path', help='Path to a trained vae model path.',
                    default='model', type=str)
parser_demo.add_argument('-device', '--device', help='torch device {"cpu" | "cuda"}',
                    default='cuda', type=str)
parser_demo.add_argument('-robot', '--robot-driver', help='choose robot driver',
                    default='jetbot', type=str)
parser_demo.add_argument('-steps', '--time-steps', help='total step.',
                    default='5000', type=int)
parser_demo.set_defaults(handler=command_demo)

if __name__ == '__main__':

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
