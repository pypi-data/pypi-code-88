from plyddl.pddlyacc import parser


def read_file(name):
    f = open( name, 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


class Plyddl:

    def __init__(self):
        self.problem = None
        self.domain = None

    def parse_domain(self, path):
        d_file = read_file(path)
        self.domain = parser.parse(d_file)

    def parse_problem(self, path):
        p_file = read_file(path)
        self.problem = parser.parse(p_file)

    def parse(self, dom_path, prob_path):
        self.parse_domain(dom_path)
        self.parse_problem(prob_path)

    def ground(self):
        if not self.domain or not self.problem:
            raise Exception('Problem and domain have to be initialised first')
        self.domain.ground_actions(self.problem.objects)

    def dynamic_ground(self, params):
        return self.domain.get_ground_actions(params, self.problem.objects)