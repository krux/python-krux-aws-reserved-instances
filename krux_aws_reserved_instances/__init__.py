######################
# Standard Libraries #
######################
from __future__ import absolute_import

#########################
# Third Party Libraries #
#########################

### The boto library
import krux_boto


class Application(krux_boto.Application):

    def __init__(self):
        ### Call to the superclass to bootstrap.
        super(Application, self).__init__(name = 'krux-aws-reserved-instances')

def main():
    app = Application()

    ec2 = app.boto.connect_ec2()

    for r in ec2.get_all_regions():
        app.logger.warn('Region: %s', r.name)


### Run the application stand alone
if __name__ == '__main__':
    main()
