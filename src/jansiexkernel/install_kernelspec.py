#!/usr/bin/env python
import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager
json ="""{"argv":["python","-m","jansiexkernel", "-f", "{connection_file}"],
 "display_name":"Elixir"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   height="300"
   viewBox="0 0 300 300"
   width="300"
   version="1.1"
   id="svg59"
   sodipodi:docname="elixir_lang_logo_icon_169207.svg"
   inkscape:version="1.2.2 (732a01da63, 2022-12-09)"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs63" />
  <sodipodi:namedview
     id="namedview61"
     pagecolor="#505050"
     bordercolor="#ffffff"
     borderopacity="1"
     inkscape:showpageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="1"
     inkscape:deskcolor="#505050"
     showgrid="false"
     inkscape:zoom="1.6191406"
     inkscape:cx="92.950543"
     inkscape:cy="138.34499"
     inkscape:window-width="1920"
     inkscape:window-height="1009"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     inkscape:current-layer="svg59" />
  <linearGradient
     id="a"
     gradientTransform="matrix(0.12970797,0,0,0.19997863,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="167.51685"
     x2="160.31"
     y1="24.393208"
     y2="320.03421">
    <stop
       offset="0"
       stop-color="#d9d8dc"
       id="stop2" />
    <stop
       offset="1"
       stop-color="#fff"
       stop-opacity=".385275"
       id="stop4" />
  </linearGradient>
  <linearGradient
     id="b"
     gradientTransform="matrix(0.11420937,0,0,0.22711641,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="199.03606"
     x2="140.0712"
     y1="21.412943"
     y2="278.40781">
    <stop
       offset="0"
       stop-color="#8d67af"
       stop-opacity=".671932"
       id="stop7" />
    <stop
       offset="1"
       stop-color="#9f8daf"
       id="stop9" />
  </linearGradient>
  <linearGradient
     id="c"
     gradientTransform="matrix(0.12266694,0,0,0.21145732,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="206.42825"
     x2="206.42825"
     y1="100.91758"
     y2="294.31174">
    <stop
       offset="0"
       stop-color="#26053d"
       stop-opacity=".761634"
       id="stop12" />
    <stop
       offset="1"
       stop-color="#b7b4b4"
       stop-opacity=".277683"
       id="stop14" />
  </linearGradient>
  <linearGradient
     id="d"
     gradientTransform="matrix(0.18477958,0,0,0.14037711,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="23.483095"
     x2="112.93069"
     y1="171.71753"
     y2="351.72263">
    <stop
       offset="0"
       stop-color="#91739f"
       stop-opacity=".45955"
       id="stop17" />
    <stop
       offset="1"
       stop-color="#32054f"
       stop-opacity=".539912"
       id="stop19" />
  </linearGradient>
  <linearGradient
     id="e"
     gradientTransform="matrix(0.14183937,0,0,0.18287462,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="226.7811"
     x2="67.803513"
     y1="317.25201"
     y2="147.4131">
    <stop
       offset="0"
       stop-color="#463d49"
       stop-opacity=".331182"
       id="stop22" />
    <stop
       offset="1"
       stop-color="#340a50"
       stop-opacity=".821388"
       id="stop24" />
  </linearGradient>
  <linearGradient
     id="f"
     gradientTransform="matrix(0.10596912,0,0,0.24477717,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="248.0164"
     x2="200.70529"
     y1="88.755211"
     y2="255.00513">
    <stop
       offset="0"
       stop-color="#715383"
       stop-opacity=".145239"
       id="stop27" />
    <stop
       offset="1"
       stop-color="#f4f4f4"
       stop-opacity=".233639"
       id="stop29" />
  </linearGradient>
  <linearGradient
     id="g"
     gradientTransform="matrix(0.09173097,0,0,0.28277061,11.409779,-1e-6)"
     gradientUnits="userSpaceOnUse"
     x1="307.5639"
     x2="156.45103"
     y1="109.963"
     y2="81.526764">
    <stop
       offset="0"
       stop-color="#a5a1a8"
       stop-opacity=".356091"
       id="stop32" />
    <stop
       offset="1"
       stop-color="#370c50"
       stop-opacity=".581975"
       id="stop34" />
  </linearGradient>
  <g
     fill-rule="evenodd"
     id="g57"
     transform="matrix(4.6574185,0,0,4.6574185,-0.21579559,0.9626099)">
    <path
       d="M 34.033696,0.16105439 C 29.38399,1.8091896 24.895482,6.6196555 20.568171,14.592452 14.077205,26.551647 5.6938102,43.545886 17.237813,57.001185 22.578416,63.226011 31.396418,66.899864 42.968724,61.08128 52.26526,56.40696 54.850738,42.992791 51.513143,36.689245 44.628358,23.686294 37.643438,20.479149 35.773012,12.415286 34.526062,7.039377 33.94629,2.9546332 34.033696,0.16105439 Z"
       fill="url(#a)"
       id="path37"
       style="fill:url(#a)" />
    <path
       d="M 34.033696,-9.5e-7 C 29.360402,1.6651252 24.871893,6.4755912 20.568171,14.431397 14.11259,26.365106 5.6938102,43.38483 17.237813,56.84013 c 5.340603,6.224826 14.045121,8.236341 18.875071,4.544505 3.148725,-2.40677 5.290239,-4.700935 6.52406,-9.534696 C 44.010778,46.467647 42.95669,39.221392 42.234421,35.892578 41.320469,31.68033 41.021325,27.057084 41.336992,22.022843 41.225762,21.88733 41.142647,21.785916 41.087645,21.718603 38.573117,18.641279 36.632762,15.960825 35.773012,12.25423 34.526062,6.8783217 33.94629,2.7935778 34.033696,-9.5e-7 Z"
       fill="url(#b)"
       id="path39"
       style="fill:url(#b)" />
    <path
       d="M 30.164134,2.0937185 C 25.811322,5.5338795 22.574907,11.304212 20.454888,19.404716 17.274859,31.555472 16.930267,42.76043 18.051811,49.277781 20.225991,61.912052 31.497649,66.707889 43.059228,60.8271 50.174379,57.207985 53.137882,49.439596 52.980879,41.00734 52.818313,32.276298 35.94623,22.381185 32.958201,15.094595 30.966183,10.236867 30.034827,5.9032421 30.164134,2.0937185 Z"
       fill="url(#c)"
       id="path41"
       style="fill:url(#c)" />
    <path
       d="m 41.199436,24.874043 c 5.220347,6.694959 6.358283,11.355459 3.413807,13.981497 -4.416714,3.93906 -15.217419,6.509155 -21.936599,1.744215 -4.479454,-3.176628 -6.174316,-9.991206 -5.084588,-20.443737 -1.849118,3.861723 -3.412567,7.773671 -4.690348,11.735849 -1.27778,3.962178 -1.650915,8.108529 -1.119404,12.439052 1.601351,3.239683 5.494817,5.403396 11.680397,6.491139 9.278371,1.631615 18.060122,0.825407 23.95271,-2.145065 3.928391,-1.980314 5.786494,-3.951651 5.574312,-5.91401 0.141766,-2.897853 -0.751847,-5.656438 -2.680832,-8.275753 -1.928988,-2.619317 -4.965472,-5.823713 -9.109455,-9.613187 z"
       fill="url(#d)"
       id="path43"
       style="fill:url(#d)" />
    <path
       d="m 20.799251,18.189006 c -0.04364,4.835125 1.199603,9.431489 3.729718,13.789093 3.795174,6.536405 8.225212,12.995204 14.854367,18.348954 4.419436,3.569167 7.950747,4.722294 10.593929,3.459382 -2.170994,3.88538 -4.479397,5.78925 -6.925211,5.711609 -3.668718,-0.11646 -8.142117,-1.719788 -15.309635,-10.333032 -4.778347,-5.742163 -8.047222,-11.17387 -9.806624,-16.295121 0.279004,-2.031676 0.574857,-4.055285 0.887559,-6.070826 0.312702,-2.015542 0.971335,-4.885561 1.975897,-8.610059 z"
       fill="url(#e)"
       id="path45"
       style="fill:url(#e)" />
    <path
       d="m 32.011273,24.824412 c 0.405511,3.938827 1.93822,10.239557 0,14.434591 -1.938221,4.195036 -10.890677,11.773476 -8.419446,18.449432 2.47123,6.675957 8.493644,5.177168 12.271355,2.100547 3.777712,-3.076623 5.799822,-8.079349 6.248034,-11.597523 0.448213,-3.518171 -1.072381,-10.287708 -1.56693,-16.17596 -0.329698,-3.9255 -0.106002,-7.291185 0.671093,-10.097054 l -1.15758,-1.456665 -6.813456,-2.017361 c -1.092388,1.614111 -1.503411,3.73411 -1.23307,6.359993 z"
       fill="url(#f)"
       id="path47"
       style="fill:url(#f)" />
    <path
       d="m 34.443394,5.3148253 c -2.205235,0.9318217 -4.294586,2.7781986 -6.268054,5.5391307 -2.960203,4.141399 -4.467906,6.623907 -3.3519,14.833191 0.744003,5.472857 1.276531,10.50778 1.597582,15.104773 L 35.964054,13.064932 C 35.613219,11.652117 35.321422,10.376166 35.088663,9.2370772 34.855905,8.0979885 34.640815,6.7905712 34.443394,5.3148253 Z"
       fill="url(#g)"
       id="path49"
       style="fill:url(#g)" />
    <path
       d="m 35.945755,13.009805 c -2.422551,1.413992 -4.299708,4.310913 -5.631469,8.690763 -1.331762,4.379852 -2.550147,10.50277 -3.655157,18.368756 1.47381,-5.003069 2.451455,-8.626771 2.932936,-10.871105 0.722221,-3.366501 0.968912,-8.127131 2.886564,-11.359156 1.278437,-2.154684 2.434144,-3.764436 3.467126,-4.829258 z"
       fill="#330a4c"
       fill-opacity="0.316321"
       id="path51" />
    <path
       d="m 24.728788,59.937995 c 3.986659,0.569558 6.071303,1.075916 6.253931,1.519073 0.273942,0.664733 -0.504655,1.272785 -2.717611,0.864177 -1.475304,-0.272404 -2.654077,-1.06682 -3.53632,-2.38325 z"
       fill="#ffffff"
       id="path53" />
    <path
       d="m 26.731652,5.3148253 c -2.192807,2.6195801 -4.092897,5.3967527 -5.700271,8.3315187 -1.607374,2.934766 -2.755892,5.124204 -3.445555,6.568313 -0.213753,1.077096 -0.318084,2.666371 -0.312993,4.767823 0.0051,2.101452 0.186856,4.438039 0.545295,7.009761 0.313817,-5.035952 1.274508,-9.924178 2.882072,-14.664678 1.607565,-4.740501 3.618049,-8.7447464 6.031452,-12.0127377 z"
       fill="#ededed"
       fill-opacity="0.603261"
       id="path55" />
  </g>
</svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/jansiexkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jansiexkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jansiexkernel')