import numpy as np

from copy import deepcopy

from Karma.PostProcessing.Lumberjack.cfg.dijet import QUANTITIES

__all__ = ["EXPANSIONS"]

EXPANSIONS = {
    # quantities
    'quantity' : [
        {
            "name": "jet1pt",
            "label": r"${p_{\mathrm{T}}^{\mathrm{jet1}}}$ /  GeV",
            "scale": "log",
            'range' : (60, 4827),
            'xs_range': (1e-10, 1e10),
            'xs_label': r"Diff. cross section $\frac{{\mathrm{{d}}^3\sigma}}{{\mathrm{{d}}{{{}}}\,\mathrm{{d}}y_{{\mathrm{{b}}}}\,\mathrm{{d}}y*}}\,\,/\,\,\mathrm{{pb}}\,\,\mathrm{{GeV}}^{{-1}}$".format(r"{p_{\mathrm{T}}^{\mathrm{jet1}}}"),
            'gen_name': "jet1MatchedGenJetPt",
            'gen_label': r"${p_{\mathrm{T}}^{\mathrm{jet1,gen}}}$ /  GeV",
            "stagger_factors": {
                "inclusive": 0,
                "YB01_YS01": 4,
                "YB01_YS12": 3,
                "YB01_YS23": -1,
                "YB12_YS01": 1,
                "YB12_YS12": 0,
                "YB23_YS01": -3,
                "YB_00_05_YS_00_05": 0,
                "YB_00_05_YS_05_10": 0,
                "YB_00_05_YS_10_15": 0,
                "YB_00_05_YS_15_20": 0,
                "YB_00_05_YS_20_25": 0,
                "YB_05_10_YS_00_05": 0,
                "YB_05_10_YS_05_10": 0,
                "YB_05_10_YS_10_15": 0,
                "YB_05_10_YS_15_20": 0,
                "YB_10_15_YS_00_05": 0,
                "YB_10_15_YS_05_10": 0,
                "YB_10_15_YS_10_15": 0,
                "YB_15_20_YS_00_05": 0,
                "YB_15_20_YS_05_10": 0,
                "YB_20_25_YS_00_05": 0,
            }
        },
        {
            "name": "jet2pt",
            "label": r"${p_{\mathrm{T}}^{\mathrm{jet2}}}$ /  GeV",
            "scale": "log",
            'range' : (60, 4827),
            'gen_name': "jet2MatchedGenJetPt",
            'gen_label': r"${p_{\mathrm{T}}^{\mathrm{jet2,gen}}}$ /  GeV",
        },
        {
            "name": "jet12ptave",
            "label": r"${\langle p_{\mathrm{T}} \rangle}_{1,2}$ / GeV",
            "scale": "log",
            'range' : (100, 4045),
            'larger_range' : (100, 25000),
            'xs_range': (5*1e-7, 1e30),
            'xs_label': r"Diff. cross section $\frac{{\mathrm{{d}}^3\sigma}}{{\mathrm{{d}}{{{}}}\,\mathrm{{d}}y_{{\mathrm{{b}}}}\,\mathrm{{d}}y*}}\,\,/\,\,\mathrm{{pb}}\,\,\mathrm{{GeV}}^{{-1}}$".format(r"{\langle p_{\mathrm{T}} \rangle}_{1,2}"),
            'gen_name': "jet12MatchedGenJetPairPtAve",
            'gen_label': r"${\langle p_{\mathrm{T}} \rangle}_{1,2}^{\mathrm{gen}}$ / GeV",
            "stagger_factors": {
                "inclusive": 0,
                "YB01_YS01": 4,
                "YB01_YS12": 3,
                "YB01_YS23": -1,
                "YB12_YS01": 1,
                "YB12_YS12": 0,
                "YB23_YS01": -3,
                "YB_00_05_YS_00_05": 1*(4-0) + 5*(4-0) - 0,  #4+3+3+3,    # D
                "YB_00_05_YS_05_10": 1*(4-1) + 5*(4-0) - 0,  #4+3+3+2,    # D
                "YB_00_05_YS_10_15": 1*(4-2) + 5*(4-0) - 0,  #3+3+3,      # v
                "YB_00_05_YS_15_20": 1*(4-3) + 5*(4-0) - 0,  #3+3+1,      # v
                "YB_00_05_YS_20_25": 1*(4-4) + 5*(4-0) - 0,  #-1,         # ^
                "YB_05_10_YS_00_05": 1*(4-0) + 5*(4-1) - 4,  #4+3+3+1,    # D
                "YB_05_10_YS_05_10": 1*(4-1) + 5*(4-1) - 4,  #4+3+3+0,    # D
                "YB_05_10_YS_10_15": 1*(4-2) + 5*(4-1) - 4,  #3+3+2,      # v
                "YB_05_10_YS_15_20": 1*(4-3) + 5*(4-1) - 4,  #3+3+0,      # v
                "YB_10_15_YS_00_05": 1*(4-0) + 5*(4-2) - 6,  #1+3,        # s
                "YB_10_15_YS_05_10": 1*(4-1) + 5*(4-2) - 6,  #1+2,        # s
                "YB_10_15_YS_10_15": 1*(4-2) + 5*(4-2) - 6,  #0,          # >
                "YB_15_20_YS_00_05": 1*(4-0) + 5*(4-3) - 6,  #1+1,        # s
                "YB_15_20_YS_05_10": 1*(4-1) + 5*(4-3) - 6,  #1+0,        # s
                "YB_20_25_YS_00_05": 1*(4-0) + 5*(4-4) - 4,  #-3,         # o
            }
        },
        {
            "name": "jet12mass",
            "label": r"${m_{\mathrm{jj}}}$ / GeV",
            "scale": "log",
            'range' : (200, 9607),
            'larger_range' : (200, 1e5/2),
            'xs_range': (1e-6, 1e17),
            'xs_label': r"Diff. cross section $\frac{{\mathrm{{d}}^3\sigma}}{{\mathrm{{d}}{{{}}}\,\mathrm{{d}}y_{{\mathrm{{b}}}}\,\mathrm{{d}}y*}}\,\,/\,\,\mathrm{{pb}}\,\,\mathrm{{GeV}}^{{-1}}$".format(r"{m_{\mathrm{jj}}}"),
            'gen_name': "jet12MatchedGenJetPairMass",
            'gen_label': r"${m_{\mathrm{jj}}^{\mathrm{gen}}}$ / GeV",
            "stagger_factors": {
                "inclusive": 0,
                "YB01_YS01": -2,
                "YB01_YS12": 2,
                "YB01_YS23": 4,
                "YB12_YS01": -3,
                "YB12_YS12": 1,
                "YB23_YS01": -3,
                "YB_00_05_YS_00_05": 1*(4-0) + 3*(4-0) - 4,  #4+3+3+3,    # D
                "YB_00_05_YS_05_10": 1*(4-1) + 3*(4-0) - 4,  #4+3+3+2,    # D
                "YB_00_05_YS_10_15": 1*(4-2) + 3*(4-0) - 4,  #3+3+3,      # v
                "YB_00_05_YS_15_20": 1*(4-3) + 3*(4-0) - 4,  #3+3+1,      # v
                "YB_00_05_YS_20_25": 1*(4-4) + 3*(4-0) - 4,  #-1,         # ^
                "YB_05_10_YS_00_05": 1*(4-0) + 3*(4-1) - 5,  #4+3+3+1,    # D
                "YB_05_10_YS_05_10": 1*(4-1) + 3*(4-1) - 5,  #4+3+3+0,    # D
                "YB_05_10_YS_10_15": 1*(4-2) + 3*(4-1) - 5,  #3+3+2,      # v
                "YB_05_10_YS_15_20": 1*(4-3) + 3*(4-1) - 5,  #3+3+0,      # v
                "YB_10_15_YS_00_05": 1*(4-0) + 3*(4-2) - 6,  #1+3,        # s
                "YB_10_15_YS_05_10": 1*(4-1) + 3*(4-2) - 6,  #1+2,        # s
                "YB_10_15_YS_10_15": 1*(4-2) + 3*(4-2) - 6,  #0,          # >
                "YB_15_20_YS_00_05": 1*(4-0) + 3*(4-3) - 6,  #1+1,        # s
                "YB_15_20_YS_05_10": 1*(4-1) + 3*(4-3) - 6,  #1+0,        # s
                "YB_20_25_YS_00_05": 1*(4-0) + 3*(4-4) - 4,  #-3,         # o
            }
        },
        {
            "name": "jet1y",
            "label": r"${y^{\mathrm{jet1}}}$",
            "scale": "linear",
            'range' : (-3, 3),
            'gen_name': "jet1MatchedGenJetY",
            'gen_label': r"$y^{\mathrm{jet1,gen}}$",
        },
        {
            "name": "jet2y",
            "label": r"${y^{\mathrm{jet2}}}$",
            "scale": "linear",
            'range' : (-3, 3),
            'gen_name': "jet2MatchedGenJetY",
            'gen_label': r"$y^{\mathrm{jet2,gen}}$",
        },
        {
            "name": "jet1phi",
            "label": r"${\phi^{\mathrm{jet1}}}$",
            "scale": "linear",
            'range' : (-np.pi, np.pi),
            'xs_range': None,
            'xs_label': "Cross section / pb",
            'gen_name': None,
            'gen_label': None,
        },
        {
            "name": "jet2phi",
            "label": r"${\phi^{\mathrm{jet2}}}$",
            "scale": "linear",
            'range' : (-np.pi, np.pi),
            'xs_range': None,
            'xs_label': "Cross section / pb",
            'gen_name': None,
            'gen_label': None,
        },
        {
            "name": "ystar",
            "label": r"${y^{\mathrm{*}}}$",
            "scale": "linear",
            'range' : (0, 3),
        },
        {
            "name": "yboost",
            "label": r"${y_{\mathrm{b}}}$",
            "scale": "linear",
            'range' : (0, 3),
        },
        {
            "name": "metOverSumET",
            "label": r"${E_{\mathrm{T}}^{\mathrm{miss}}}/\sum_i{E_{\mathrm{T}}^{\mathrm{i}}}$",
            "scale": "linear",
            'range' : (0, 1),
            'xs_range': None,
            'xs_label': "Diff. cross section / pb",
        },
        {
            "name": "npv",
            "label": r"# of primary vertices $n_{\mathrm{PV}}$",
            "scale": "linear",
            'range' : (-0.5, 80.5),
        },
        {
            "name": "npvGood",
            "label": r"# of good primary vertices $n_{\mathrm{PV,good}}$",
            "scale": "linear",
            'range' : (-0.5, 80.5),
        },
        {
            "name": "nPUMean",
            "label": r"Expected pileup $\mu$",
            "scale": "linear",
            'range' : (-0.5, 80.5),
        },
        {
            "name": "jet12DeltaPhi",
            "label": r"$\Delta\phi_{1,2}$",
            "scale": "linear",
            'range' : (0, np.pi),
        },
        {
            "name": "jet12DeltaR",
            "label": r"$\Delta R_{1,2}$",
            "scale": "linear",
            'range' : (0, 8),
        },
    ],
    # phase space regions (in y_boost, y_star)
    'ybys' : [
        {
            "name": "YB01_YS01",
            "label": r"YB01_YS01",
            "color": "royalblue",
            "marker": "D",
            "marker_style": "full",
        },
        {
            "name": "YB01_YS12",
            "label": r"YB01_YS12",
            "color": "forestgreen",
            "marker": "v",
            "marker_style": "full",
        },
        {
            "name": "YB01_YS23",
            "label": r"YB01_YS23",
            "color": "darkred",
            "marker": "^",
            "marker_style": "full",
        },
        {
            "name": "YB12_YS01",
            "label": r"YB12_YS01",
            "color": "darkorchid",
            "marker": "s",
            "marker_style": "full",
        },
        {
            "name": "YB12_YS12",
            "label": r"YB12_YS12",
            "color": "orange",
            "marker": ">",
            "marker_style": "full",
        },
        {
            "name": "YB23_YS01",
            "label": r"YB23_YS01",
            "color": "darkturquoise",
            "marker": "o",
            "marker_style": "full",
        },
        {
            "name": "inclusive",
            "label": r"inclusive",
            "color": "k",
            "marker": "o",
            "marker_style": "empty",
        },
    ],
    # phase space regions (in y_boost, y_star)
    'ybys_narrow' : [
        {"name": "YB_00_05_YS_00_05", "label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$, $0   \leq y{{*}} < 0.5$", "yb_label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$", "ys_label": r"$0   \leq y{{*}} < 0.5$", "color": "#5c15b6", "marker": "D", "marker_style": "full", "area": 0.25},   # YB01_YS01
        {"name": "YB_00_05_YS_05_10", "label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$, $0.5 \leq y{{*}} <   1$", "yb_label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$", "ys_label": r"$0.5 \leq y{{*}} <   1$", "color": "#2659a2", "marker": "D", "marker_style": "full", "area": 0.25},   # YB01_YS01
        {"name": "YB_00_05_YS_10_15", "label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$, $1   \leq y{{*}} < 1.5$", "yb_label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$", "ys_label": r"$1   \leq y{{*}} < 1.5$", "color": "#139913", "marker": "v", "marker_style": "full", "area": 0.25},   # YB01_YS12
        {"name": "YB_00_05_YS_15_20", "label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$, $1.5 \leq y{{*}} <   2$", "yb_label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$", "ys_label": r"$1.5 \leq y{{*}} <   2$", "color": "#c55200", "marker": "v", "marker_style": "full", "area": 0.25},   # YB01_YS12
        {"name": "YB_00_05_YS_20_25", "label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$, $2   \leq y{{*}} < 2.5$", "yb_label": r"$0   \leq y_{{\mathrm{{b}}}} < 0.5$", "ys_label": r"$2   \leq y{{*}} < 2.5$", "color": "#a11313", "marker": "^", "marker_style": "full", "area": 0.25},   # YB01_YS23
        {"name": "YB_05_10_YS_00_05", "label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$, $0   \leq y{{*}} < 0.5$", "yb_label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$", "ys_label": r"$0   \leq y{{*}} < 0.5$", "color": "#7959c4", "marker": "D", "marker_style": "full", "area": 0.25},   # YB01_YS01
        {"name": "YB_05_10_YS_05_10", "label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$, $0.5 \leq y{{*}} <   1$", "yb_label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$", "ys_label": r"$0.5 \leq y{{*}} <   1$", "color": "#3e98b2", "marker": "D", "marker_style": "full", "area": 0.25},   # YB01_YS01
        {"name": "YB_05_10_YS_10_15", "label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$, $1   \leq y{{*}} < 1.5$", "yb_label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$", "ys_label": r"$1   \leq y{{*}} < 1.5$", "color": "#51c230", "marker": "v", "marker_style": "full", "area": 0.25},   # YB01_YS12
        {"name": "YB_05_10_YS_15_20", "label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$, $1.5 \leq y{{*}} <   2$", "yb_label": r"$0.5 \leq y_{{\mathrm{{b}}}} <   1$", "ys_label": r"$1.5 \leq y{{*}} <   2$", "color": "#ffa500", "marker": "v", "marker_style": "full", "area": 0.25},   # YB01_YS12
        {"name": "YB_10_15_YS_00_05", "label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$, $0   \leq y{{*}} < 0.5$", "yb_label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$", "ys_label": r"$0   \leq y{{*}} < 0.5$", "color": "#9983cf", "marker": "s", "marker_style": "full", "area": 0.25},   # YB12_YS01
        {"name": "YB_10_15_YS_05_10", "label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$, $0.5 \leq y{{*}} <   1$", "yb_label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$", "ys_label": r"$0.5 \leq y{{*}} <   1$", "color": "#67b4cb", "marker": "s", "marker_style": "full", "area": 0.25},   # YB12_YS01
        {"name": "YB_10_15_YS_10_15", "label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$, $1   \leq y{{*}} < 1.5$", "yb_label": r"$1   \leq y_{{\mathrm{{b}}}} < 1.5$", "ys_label": r"$1   \leq y{{*}} < 1.5$", "color": "#8def56", "marker": ">", "marker_style": "full", "area": 0.25},   # YB12_YS12
        {"name": "YB_15_20_YS_00_05", "label": r"$1.5 \leq y_{{\mathrm{{b}}}} <   2$, $0   \leq y{{*}} < 0.5$", "yb_label": r"$1.5 \leq y_{{\mathrm{{b}}}} <   2$", "ys_label": r"$0   \leq y{{*}} < 0.5$", "color": "#c6b2e2", "marker": "s", "marker_style": "full", "area": 0.25},   # YB12_YS01
        {"name": "YB_15_20_YS_05_10", "label": r"$1.5 \leq y_{{\mathrm{{b}}}} <   2$, $0.5 \leq y{{*}} <   1$", "yb_label": r"$1.5 \leq y_{{\mathrm{{b}}}} <   2$", "ys_label": r"$0.5 \leq y{{*}} <   1$", "color": "#a0eaff", "marker": "s", "marker_style": "full", "area": 0.25},   # YB12_YS01
        {"name": "YB_20_25_YS_00_05", "label": r"$2   \leq y_{{\mathrm{{b}}}} < 2.5$, $0   \leq y{{*}} < 0.5$", "yb_label": r"$2   \leq y_{{\mathrm{{b}}}} < 2.5$", "ys_label": r"$0   \leq y{{*}} < 0.5$", "color": "#fab0ff", "marker": "o", "marker_style": "full", "area": 0.25},   # YB23_YS01
        {
            "name": "inclusive",
            "label": r"inclusive",
            "yb_label": r"$y_{\mathrm{b}}$-inclusive",
            "ys_label": r"$y{*}$-inclusive",
            "color": "k",
            "marker": "o",
            "marker_style": "empty",
        },
    ],
    # trigger paths
    'trigger_ak4' : [
        {
            "name": "HLT_PFJet40",
            "preceding_path_name": None,
            "label": r"PFJet40",
            "color": "#1b09aa",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 10000.0,
            'lumi_ub': 48714.091,  # Run2016G
        },
        {
            "name": "HLT_PFJet60",
            "preceding_path_name": "HLT_PFJet40",
            "label": r"PFJet60",
            "color": "#094aaa",
            "marker": "D",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 123328.102,  # Run2016G
        },
        {
            "name": "HLT_PFJet80",
            "preceding_path_name": "HLT_PFJet60",
            "label": r"PFJet80",
            "color": "#0bd1d1",
            "marker": "v",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 369296.644,  # Run2016G
        },
        {
            "name": "HLT_PFJet140",
            "preceding_path_name": "HLT_PFJet80",
            "label": r"PFJet140",
            "color": "#0ce41f",
            "marker": "^",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 3618461.972,  # Run2016G
        },
        {
            "name": "HLT_PFJet200",
            "preceding_path_name": "HLT_PFJet140",
            "label": r"PFJet200",
            "color": "#dee40c",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 100.0,
            'lumi_ub': 11962959.393,  # Run2016G
        },
        {
            "name": "HLT_PFJet260",
            "preceding_path_name": "HLT_PFJet200",
            "label": r"PFJet260",
            "color": "#e4ac0c",
            "marker": ">",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 102345547.894,  # Run2016G
        },
        {
            "name": "HLT_PFJet320",
            "preceding_path_name": "HLT_PFJet260",
            "label": r"PFJet320",
            "color": "#ed690c",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 310001081.812,  # Run2016G
        },
        {
            "name": "HLT_PFJet400",
            "preceding_path_name": "HLT_PFJet320",
            "label": r"PFJet400",
            "color": "#ed360c",
            "marker": "x",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 918960478.743,  # Run2016G
        },
        {
            "name": "HLT_PFJet450",
            "preceding_path_name": "HLT_PFJet400",
            "label": r"PFJet450",
            "color": "#d1110b",
            "marker": "d",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
        {
            "name": "HLT_PFJet500",
            "preceding_path_name": "HLT_PFJet450",
            "label": r"PFJet500",
            "color": "#a52509",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
        {
            "name": "all",
            "preceding_path_name": None,
            "label": r"all triggers",
            "color": "k",
            "marker": "o",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
    ],
    'trigger_ak8' : [
        {
            "name": "HLT_AK8PFJet40",
            "label": r"AK8PFJet40",
            "color": "#1b09aa",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 10000.0,
            'lumi_ub': 9742.818,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet60",
            "label": r"AK8PFJet60",
            "color": "#094aaa",
            "marker": "D",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 61664.051,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet80",
            "label": r"AK8PFJet80",
            "color": "#0bd1d1",
            "marker": "v",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 184648.322,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet140",
            "label": r"AK8PFJet140",
            "color": "#0ce41f",
            "marker": "^",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 1809230.986,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet200",
            "label": r"AK8PFJet200",
            "color": "#dee40c",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 100.0,
            'lumi_ub': 11962959.393,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet260",
            "label": r"AK8PFJet260",
            "color": "#e4ac0c",
            "marker": ">",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 102345547.894,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet320",
            "label": r"AK8PFJet320",
            "color": "#ed690c",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 310001081.812,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet400",
            "label": r"AK8PFJet400",
            "color": "#ed360c",
            "marker": "x",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 918960478.743,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet450",
            "label": r"AK8PFJet450",
            "color": "#d1110b",
            "marker": "d",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
        {
            "name": "HLT_AK8PFJet500",
            "label": r"AK8PFJet500",
            "color": "#a52509",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
        {
            "name": "all",
            "label": r"all triggers",
            "color": "k",
            "marker": "o",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 7544015569.439,  # Run2016G
        },
    ],
    # trigger paths
    'trigger_dijet' : [
        {
            "name": "HLT_DiPFJetAve40",
            "label": r"DiPFJetAve40",
            "color": "#1b09aa",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 10000.0,
            'lumi_ub': 11311.920,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve60",
            "label": r"DiPFJetAve60",
            "color": "#094aaa",
            "marker": "D",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 350986.611,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve80",
            "label": r"DiPFJetAve80",
            "color": "#0bd1d1",
            "marker": "v",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 340824.353,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve140",
            "label": r"DiPFJetAve140",
            "color": "#0ce41f",
            "marker": "^",
            'marker_style': 'full',
            'l1_factor': 1000.0,
            'lumi_ub': 3618461.972,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve200",
            "label": r"DiPFJetAve200",
            "color": "#dee40c",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 100.0,
            'lumi_ub': 17873786.697,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve260",
            "label": r"DiPFJetAve260",
            "color": "#e4ac0c",
            "marker": ">",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 107807705.356,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve320",
            "label": r"DiPFJetAve320",
            "color": "#ed690c",
            "marker": "o",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 594238641.781,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve400",
            "label": r"DiPFJetAve400",
            "color": "#ed360c",
            "marker": "x",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 1705794763.427,  # Run2016G
        },
        {
            "name": "HLT_DiPFJetAve500",
            "label": r"DiPFJetAve500",
            "color": "#a52509",
            "marker": "s",
            'marker_style': 'full',
            'l1_factor': 1.0,
            'lumi_ub': 5736356853.437,  # Run2016G
        },
        {
            "name": "all",
            "label": r"all triggers",
            "color": "k",
            "marker": "o",
            'marker_style': 'empty',
            'l1_factor': 1.0,
            'lumi_ub': 5736356853.437,  # Run2016G
        },
    ],
    # event yields (2D binnings)
    'occupancy': [
        {
            "name": "absjet2y_vs_absjet1y",
            #
            "x_quantity": "absjet1y",
            "x_label": r"$|{y^{\mathrm{jet1}}}|$",
            "x_scale": "linear",
            #
            "y_quantity": "absjet2y",
            "y_label": r"$|{y^{\mathrm{jet2}}}|$",
            "y_scale": "linear",
        },
        {
            "name": "ystar_vs_yboost",
            #
            "x_quantity": "yboost",
            "x_label": r"$y_{\mathrm{b}}$",
            "x_scale": "linear",
            #
            "y_quantity": "ystar",
            "y_label": r"$y^{*}$",
            "y_scale": "linear",
        },
        {
            "name": "jet1phi_vs_jet1eta",
            #
            "x_quantity": "jet1eta",
            "x_label": r"$\eta^{\mathrm{jet1}}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet1phi",
            "y_label": r"$\phi^{\mathrm{jet1}}$",
            "y_scale": "linear",
        },
        {
            "name": "jet1pt_narrow_vs_jet1eta",
            #
            "x_quantity": "jet1eta",
            "x_label": r"$\eta^{\mathrm{jet1}}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet1pt_narrow",
            "y_label": r"$p_{\mathrm{T}}^{\mathrm{jet1}}$",
            "y_scale": "log",
        },
        {
            "name": "jet12ptave_narrow_vs_ystar",
            #
            "x_quantity": "ystar",
            "x_label": r"$y^{*}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet12ptave_narrow",
            "y_label": r"${\langle p_{\mathrm{T}} \rangle}_{1,2}$ / GeV",
            "y_scale": "log",
        },
        {
            "name": "jet12ptave_narrow_vs_yboost",
            #
            "x_quantity": "yboost",
            "x_label": r"$y^{\mathrm{b}}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet12ptave_narrow",
            "y_label": r"${\langle p_{\mathrm{T}} \rangle}_{1,2}$ / GeV",
            "y_scale": "log",
        },
        {
            "name": "jet1pt_wide_vs_jet1eta",
            #
            "x_quantity": "jet1eta",
            "x_label": r"$\eta^{\mathrm{jet1}}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet1pt_wide",
            "y_label": r"$p_{\mathrm{T}}^{\mathrm{jet1}}$",
            "y_scale": "log",
        },
        {
            "name": "jet12ptave_wide_vs_ystar",
            #
            "x_quantity": "ystar",
            "x_label": r"$y^{*}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet12ptave_wide",
            "y_label": r"${\langle p_{\mathrm{T}} \rangle}_{1,2}$ / GeV",
            "y_scale": "log",
        },
        {
            "name": "jet12ptave_wide_vs_yboost",
            #
            "x_quantity": "yboost",
            "x_label": r"$y^{\mathrm{b}}$",
            "x_scale": "linear",
            #
            "y_quantity": "jet12ptave_wide",
            "y_label": r"${\langle p_{\mathrm{T}} \rangle}_{1,2}$ / GeV",
            "y_scale": "log",
        },
    ],
    # Particle Flow (PF) energy fractions
    'pf_fraction': [
        {
            "name": "ChargedHadronFraction",
            "label": r"PF charged hadron fraction",
            "scale": "log",
            "color": "red",
            "marker": "o",
            "marker_style": "full",
        },
        {
            "name": "PhotonFraction",
            "label": r"PF photon fraction",
            "scale": "log",
            "color": "royalblue",
            "marker": "s",
            "marker_style": "full",
        },
        {
            "name": "NeutralHadronFraction",
            "label": r"PF neutral hadron fraction",
            "scale": "log",
            "color": "green",
            "marker": "D",
            "marker_style": "full",
        },
        {
            "name": "MuonFraction",
            "label": r"PF muon fraction",
            "scale": "log",
            "color": "teal",
            "marker": "v",
            "marker_style": "full",
        },
        {
            "name": "ElectronFraction",
            "label": r"PF electron fraction",
            "scale": "log",
            "color": "orange",
            "marker": "^",
            "marker_style": "full",
        },
        # HF fractions
        {
            "name": "HFHadronFraction",
            "label": r"PF HF hadron fraction",
            "scale": "log",
            "color": "mediumorchid",
            "marker": "s",
            "marker_style": "empty",
        },
        {
            "name": "HFEMFraction",
            "label": r"PF HF electromagnetic fraction",
            "scale": "log",
            "color": "darkgoldenrod",
            "marker": "o",
            "marker_style": "empty",
        },
    ],
    # leading jet pair flavor fractions
    'flavor_fraction': [
        {
            "name": "Flavor_GG",
            "label": r"$\mathrm{g}\mathrm{g}$",
            "scale": "log",
            "color": "orange",
        },
        {
            "name": "Flavor_QG",
            "label": r"$\mathrm{q}\mathrm{g}$, $\mathrm{g}\mathrm{q}$",
            "scale": "log",
            "color": "#328DCA",
        },
        {
            "name": "Flavor_QQ_pp_ii",
            "label": r"$\mathrm{q}_\mathrm{i} \mathrm{q}_\mathrm{i}$",
            "scale": "log",
            "color": "lightgreen",
        },
        {
            "name": "Flavor_QQ_pp_ij",
            "label": r"$\mathrm{q}_\mathrm{i} \mathrm{q}_\mathrm{j}$",
            "scale": "log",
            "color": "forestgreen",
        },
        {
            "name": "Flavor_QQ_ap_ii",
            "label": r"$\mathrm{q}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{i}$",
            "scale": "log",
            "color": "salmon",
        },
        {
            "name": "Flavor_QQ_ap_ij",
            "label": r"$\mathrm{q}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{j}$",
            "scale": "log",
            "color": "firebrick",
        },
        {
            "name": "Flavor_QQ_aa_ii",
            "label": r"$\overline{\mathrm{q}}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{i}$",
            "scale": "log",
            "color": "plum",
        },
        {
            "name": "Flavor_QQ_aa_ij",
            "label": r"$\overline{\mathrm{q}}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{j}$",
            "scale": "log",
            "color": "mediumorchid",
        },
    ],
    # QCD subprocess fractions
    'qcd_subprocess_fraction': [
        {
            "name": "QCDSubprocess_GG",
            "label": r"$\mathrm{g}\mathrm{g}$",
            "scale": "log",
            #"color": "orange",
            "color": "#2079B4",
        },
        {
            "name": "QCDSubprocess_QG_xq_gt_xg",
            "label": r"$\mathrm{g}\mathrm{q}$ ($x_{\mathrm{g}} \leq x_{\mathrm{q}}$)",
            "scale": "log",
            #"color": "#7EB5DA",
            "color": "#B0DD8B",
        },
        {
            "name": "QCDSubprocess_QG_xg_gt_xq",
            "label": r"$\mathrm{g}\mathrm{q}$ ($x_{\mathrm{g}} > x_{\mathrm{q}}$)",
            "scale": "log",
            #"color": "#328DCA",
            "color": "#36A12E",
        },
        {
            "name": "QCDSubprocess_QQ_pp_ii",
            "label": r"$\mathrm{q}_\mathrm{i} \mathrm{q}_\mathrm{i}$",
            "scale": "log",
            #"color": "lightgreen",
            "color": "#C8AFD5",
        },
        {
            "name": "QCDSubprocess_QQ_pp_ij",
            "label": r"$\mathrm{q}_\mathrm{i} \mathrm{q}_\mathrm{j}$",
            "scale": "log",
            #"color": "forestgreen",
            "color": "#6C409A",
        },
        {
            "name": "QCDSubprocess_QQ_ap_ii",
            "label": r"$\mathrm{q}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{i}$",
            "scale": "log",
            #"color": "salmon",
            "color": "#FB9898",
        },
        {
            "name": "QCDSubprocess_QQ_ap_ij",
            "label": r"$\mathrm{q}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{j}$",
            "scale": "log",
            #"color": "firebrick",
            "color": "#E31B1C",
        },
        #{
        #    "name": "QCDSubprocess_QQ_aa_ii",
        #    "label": r"$\overline{\mathrm{q}}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{i}$",
        #    "scale": "log",
        #    "color": "plum",
        #},
        #{
        #    "name": "QCDSubprocess_QQ_aa_ij",
        #    "label": r"$\overline{\mathrm{q}}_\mathrm{i} \overline{\mathrm{q}}_\mathrm{j}$",
        #    "scale": "log",
        #    "color": "mediumorchid",
        #},
    ],
    # QCD subsamples
    'mc_subsample': [
        {"name": "QCD_Pt_15to30"     , "xs": 1820000000 , "n_events": 39898460 },
        {"name": "QCD_Pt_30to50"     , "xs": 138900000  , "n_events": 9980050  },
        {"name": "QCD_Pt_50to80"     , "xs": 19100000   , "n_events": 9954370  },
        {"name": "QCD_Pt_80to120"    , "xs": 2735000    , "n_events": 6986740  },
        {"name": "QCD_Pt_120to170"   , "xs": 467500     , "n_events": 6708572  },
        {"name": "QCD_Pt_170to300"   , "xs": 117400     , "n_events": 6958708  },
        {"name": "QCD_Pt_300to470"   , "xs": 7753       , "n_events": 4150588  },
        {"name": "QCD_Pt_470to600"   , "xs": 642.1      , "n_events": 3959986  },
        {"name": "QCD_Pt_600to800"   , "xs": 185.9      , "n_events": 3896412  },
        {"name": "QCD_Pt_800to1000"  , "xs": 32.05      , "n_events": 3992112  },
        {"name": "QCD_Pt_1000to1400" , "xs": 9.365      , "n_events": 2999069  },
        {"name": "QCD_Pt_1400to1800" , "xs": 0.8398     , "n_events": 396409   },
        {"name": "QCD_Pt_1800to2400" , "xs": 0.1124     , "n_events": 397660   },
        {"name": "QCD_Pt_2400to3200" , "xs": 0.006752   , "n_events": 399226   },
    ],
}


# expand 'quantity' expansions with bifferent binnings (e.g. 'wide', 'narrow', ...)
for _expansion in EXPANSIONS['quantity']:
    if _expansion["name"] in ('jet1pt', 'jet12ptave', 'jet12mass'):
        for _bin_suffix in ('narrow', 'wide'):
            _suffixed_expansion = deepcopy(_expansion)
            _suffixed_expansion['name'] = "{}_{}".format(_suffixed_expansion['name'], _bin_suffix)
            _suffixed_expansion['gen_name'] = "{}_{}".format(_suffixed_expansion['gen_name'], _bin_suffix)
            EXPANSIONS['quantity'].append(_suffixed_expansion)

# generate 'gen_quantity' expansions from 'quantity'
EXPANSIONS['gen_quantity'] = []
for _expansion in EXPANSIONS['quantity']:
    if 'gen_name' in _expansion:
        EXPANSIONS['gen_quantity'].append(
            dict(_expansion, name=_expansion['gen_name'], label=_expansion['gen_label'], reco_name=_expansion['name'], reco_label=_expansion['label'])
        )
        del EXPANSIONS['gen_quantity'][-1]['gen_name']
        del EXPANSIONS['gen_quantity'][-1]['gen_label']

# programatically fill in the defined quantity ranges for 'occupancy' axes
for _expansion in EXPANSIONS['occupancy']:
    _expansion['x_range'] = QUANTITIES['global'][_expansion['x_quantity']].range
    _expansion['y_range'] = QUANTITIES['global'][_expansion['y_quantity']].range
