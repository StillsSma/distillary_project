class LocationListView(LoginRequiredMixin, ListView):
    model = Location

class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name']
    success_url = reverse_lazy("location_list_view")

class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['name']
    success_url = reverse_lazy("location_list_view")

class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy("location_list_view")
