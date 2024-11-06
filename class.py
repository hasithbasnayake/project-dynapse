@dataclass
class Patch:
    Pix: Optional[np.ndarray] = None  # [x,y] represents the size of the image patch in pixels
    Ang: Optional[np.ndarray] = None  # [x,y] represents the size of the image patch in angular dimensions

@dataclass
class Image:
    Pix: Optional[np.ndarray] = None  # [x,y] represents the size of the image in pixels
    Ang: Optional[np.ndarray] = None  # [x,y] represents the size of the image in angular dimensions


@dataclass
class Kernel:
    @dataclass
    class OFF:
        Pix: Optional[np.ndarray] = None # numpy array, [x, y]
        Ang: Optional[np.ndarray] = None # numpy array, [x, y]

    @dataclass
    class ON:
        Pix: Optional[np.ndarray] = None # numpy array, [x, y]
        Ang: Optional[np.ndarray] = None # numpy array, [x, y]

class SigmaCentreSurround:
    @dataclass
    class OFF:
        Pix: Optional[np.ndarray] = None # numpy array, [x, y]
        Ang: Optional[np.ndarray] = None # numpy array, [x, y]

    @dataclass
    class ON:
        Pix: Optional[np.ndarray] = None # numpy array, [x, y]
        Ang: Optional[np.ndarray] = None # numpy array, [x, y]

class DifferenceOfGaussians:
    @dataclass
    class Size:
        Pix: Optional[np.ndarray] = None # numpy array, [x, y]
        Ang: Optional[np.ndarray] = None # numpy array, [x, y]
    @dataclass
    class Centre:
        @dataclass
        class Sigma:
            Pix: Optional[np.ndarray] = None # numpy array, [x, y]
            Ang: Optional[np.ndarray] = None # numpy array, [x, y]
        Kernel: Optional[np.ndarray] = None # numpy array, [x, y]

    @dataclass
    class Surround:
        @dataclass
        class Sigma:
            Pix: Optional[np.ndarray] = None # numpy array, [x, y]
            Ang: Optional[np.ndarray] = None # numpy array, [x, y]
        Kernel: Optional[np.ndarray] = None # numpy array, [x, y]

    Kernel: Optional[np.ndarray] = None # numpy array, [x, y]