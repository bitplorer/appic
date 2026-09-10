"""Page unit — testimonials.py → Testimonials. Owned kit, shell=False."""
from __future__ import annotations

from components.testimonials import Testimonials as TestimonialsCard


class Testimonials(TestimonialsCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
