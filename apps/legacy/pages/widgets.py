from eestecnet.widgets import button_for_modal, elastic_grid, piece_of_information


class AdminOptions(object):
    def get_context_data(self, **kwargs):
        context = super(AdminOptions, self).get_context_data(**kwargs)
        if not self.request.user.is_authenticated():
            return context
        context['adminoptions'] = [button_for_modal(option[0], option[1]) for option
                                   in
                                   self.adminoptions()]
        return context


class Grids(object):
    def get_context_data(self, **kwargs):
        context = super(Grids, self).get_context_data(**kwargs)
        context['grids'] = [elastic_grid(option[0], option[1], option[2]) for option in
                            self.grids()]
        return context


class Information(object):
    def get_context_data(self, **kwargs):
        context = super(Information, self).get_context_data(**kwargs)
        context['information'] = [piece_of_information(option[0], option[1]) for option
                                  in self.information()]
        return context

