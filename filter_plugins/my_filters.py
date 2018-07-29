class FilterModule(object):
    def filters(self):
        return {
            'net_int_filter': self.net_int_filter,
        }

    def net_int_filter(self, interfaces):
        ret = []
        for int_type, ints in interfaces.items():
            for int_id, int_val in ints.items():
                ret_dict = {}
                ret_dict["name"] = '%s%s' % (int_type, int_id)
                for k, v in int_val.items():
                        ret_dict[k] = v
                ret.append(ret_dict)
        return ret
