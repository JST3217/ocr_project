import csv
import glob


myOutputs = []
for report in glob.glob('Outputs/*.txt'):
    myOutputs.append(report)

with open('signal_conditioning_results.csv', mode='w') as sigcon:
    sigcon_writer = csv.writer(sigcon, delimiter=',', lineterminator='\n')
    sigcon_writer.writerow(["Robot", "Report No.", "Master Sine Offset (mV)", "Master Cosine Offset (mV)", "Master Phase Adjust", "Nonius Sine Offset (mV)", "Nonius Cosine Offset (mV)", "Nonius Phase Adjust"])

    for report in myOutputs:

        robot_col = report[8:26]
        report_col = report[27:47]

        with open(report) as report_entry:
            line = report_entry.readlines()
            master_sin_offset = float(line[0])
            master_cos_offset = float(line[1])
            master_pha_adjust = float(line[2])

            nonius_sin_offset = float(line[3])
            nonius_cos_offset = float(line[4])
            nonius_pha_offset = float(line[5])

            sigcon_writer.writerow([robot_col, report_col, master_sin_offset, master_cos_offset, master_pha_adjust, nonius_sin_offset, nonius_cos_offset, nonius_pha_offset])