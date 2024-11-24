from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit

from super_scad_ellipse.d3.Ellipsoid import Ellipsoid


class ImperialEllipsoid(ScadWidget):
    """
    Widget for creating imperial ellipsoids.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius_x: float | None = None,
                 radius_y: float | None = None,
                 radius_z: float | None = None,
                 diameter_x: float | None = None,
                 diameter_y: float | None = None,
                 diameter_z: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self._radius_x: float | None = radius_x
        self._radius_y: float | None = radius_y
        self._radius_z: float | None = radius_z
        self._diameter_x: float | None = diameter_x
        self._diameter_y: float | None = diameter_y
        self._diameter_z: float | None = diameter_z
        self._fa: float | None = fa
        self._fs: float | None = fs
        self._fn: int | None = fn

        self.imperial_ellipsoid: Ellipsoid | None = None
        """
        The imperial ellipsoid.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_ellipsoid = Ellipsoid(radius_x=self._radius_x,
                                            radius_y=self._radius_y,
                                            radius_z=self._radius_z,
                                            diameter_x=self._diameter_x,
                                            diameter_y=self._diameter_y,
                                            diameter_z=self._diameter_z,
                                            fa=self._fa,
                                            fs=self._fs,
                                            fn=self._fn)

        return self.imperial_ellipsoid

# ----------------------------------------------------------------------------------------------------------------------
