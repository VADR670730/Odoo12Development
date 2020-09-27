from odoo import models, api
import base64
import io


class CurriculumVitaeExcelReport(models.Model):
    _name = 'report.curriculum_vitae.curriculum_vitae_excel_report_template'
    _inherit = 'report.report_xlsx.abstract'

    @api.multi
    def generate_xlsx_report(self, workbook, data, lines):
        name_format = workbook.add_format({'font_size': 16, 'bold': True,
                                           'align': 'center', 'valign': 'vcenter'})
        header_format = workbook.add_format({'font_size': 14, 'bold': True,
                                             'bg_color': 'green', 'color': 'white'})
        label_format = workbook.add_format({'font_size': 11, 'bold': True})

        sheet = workbook.add_worksheet("CV Form")
        sheet.set_column(0, 5, 20)
        sheet.set_row(0, 110)

        sheet.merge_range('A1:E1', lines.name, name_format)

        cv_image = lines.image
        image_data = base64.b64decode(cv_image)
        image = io.BytesIO(image_data)
        sheet.insert_image('F1', 'cv_image.png', {'image_data': image, 'x_scale': 0.6, 'y_scale': 0.6})

        sheet.merge_range('A2:F2', 'Personal Particulars', header_format)
        sheet.write('A3', 'Mobile', label_format)
        sheet.merge_range('B3:F3', lines.mobile)
        sheet.write('A4', 'Email', label_format)
        sheet.merge_range('B4:F4', lines.email)
        sheet.write('A5', 'Age', label_format)
        sheet.merge_range('B5:F5', lines.age,
                          workbook.add_format({'align': 'left'}))
        sheet.write('A6', 'Date of Birth', label_format)
        sheet.merge_range('B6:F6', lines.date_of_birth,
                          workbook.add_format({'align': 'left', 'num_format': 'dd mmm yyyy'}))
        sheet.write('A7', 'NRC', label_format)
        sheet.merge_range('B7:F7', lines.nrc)

        sheet.write('A8', 'Nationality', label_format)
        sheet.merge_range('B8:F8', lines.nationality)
        sheet.write('A9', 'Religion', label_format)
        sheet.merge_range('B9:F9', lines.religion)
        sheet.write('A10', 'Gender', label_format)
        sheet.merge_range('B10:F10', lines.gender)
        sheet.write('A11', 'Current Address', label_format)
        sheet.merge_range('B11:F11', lines.current_address)
        sheet.write('A12', 'Marital Status', label_format)
        sheet.merge_range('B12:F12', lines.marital_status)

        sheet.merge_range('A13:F13', 'Career Objectives', header_format)
        sheet.set_row(13, 70)
        sheet.merge_range('A14:F14', lines.objectives, workbook.add_format({'valign': 'top'}))

        row = 14
        column = 0
        sheet.merge_range(row, column, row, column + 5, 'Education Background', header_format)

        row += 1
        sheet.write(row, column, 'Name', label_format)
        column += 1
        sheet.write(row, column, 'Country', label_format)
        column += 1
        sheet.write(row, column, 'Certification', label_format)
        column += 1
        sheet.write(row, column, 'Description', label_format)
        column += 1
        sheet.write(row, column, 'Period From', label_format)
        column += 1
        sheet.write(row, column, 'Period To', label_format)

        row += 1
        column = 0
        for ebl in lines.education_background_lines:
            sheet.write(row, column, ebl.name)
            column += 1
            sheet.write(row, column, ebl.country)
            column += 1
            sheet.write(row, column, ebl.certification)
            column += 1
            sheet.write(row, column, ebl.description)
            column += 1
            sheet.write(row, column, ebl.period_from, workbook.add_format({'num_format': 'dd/mm/yyyy'}))
            column += 1
            sheet.write(row, column, ebl.period_to, workbook.add_format({'num_format': 'dd/mm/yyyy'}))

            row += 1
            column = 0

        eh_row = row
        eh_column = column
        sheet.merge_range(eh_row, eh_column, eh_row, eh_column + 5, "Employment History", header_format)

        eh_row += 1
        sheet.write(eh_row, eh_column, "Company Name", label_format)
        eh_column += 1
        sheet.write(eh_row, eh_column, "Position", label_format)
        eh_column += 1
        sheet.write(eh_row, eh_column, "Responsibilities", label_format)
        eh_column += 1
        sheet.write(eh_row, eh_column, "Period From", label_format)
        eh_column += 1
        sheet.write(eh_row, eh_column, "Period To", label_format)
        eh_column += 1
        sheet.write(eh_row, eh_column, "Description", label_format)

        eh_row += 1
        eh_column = 0
        for ehl in lines.employment_history_lines:
            sheet.write(eh_row, eh_column, ehl.name)
            eh_column += 1
            sheet.write(eh_row, eh_column, ehl.position)
            eh_column += 1
            sheet.write(eh_row, eh_column, ehl.responsibilities)
            eh_column += 1
            sheet.write(eh_row, eh_column, ehl.period_from,
                        workbook.add_format({'num_format': 'dd/mm/yyyy'}))
            eh_column += 1
            sheet.write(eh_row, eh_column, ehl.period_to,
                        workbook.add_format({'num_format': 'dd/mm/yyyy'}))
            eh_column += 1
            sheet.write(eh_row, eh_column, ehl.description)

            eh_row += 1
            eh_column = 0

        pe_row = eh_row
        pe_column = 0
        sheet.merge_range(pe_row, pe_column, pe_row, pe_column + 5, 'Project Experiences', header_format)

        pe_row += 1
        sheet.write(pe_row, pe_column, 'Project Name', label_format)
        pe_column += 1
        sheet.write(pe_row, pe_column, 'Position', label_format)
        pe_column += 1
        sheet.write(pe_row, pe_column, 'Responsibilities', label_format)
        pe_column += 1
        sheet.write(pe_row, pe_column, 'Programming Languages', label_format)
        pe_column += 1
        sheet.write(pe_row, pe_column, 'Period From', label_format)
        pe_column += 1
        sheet.write(pe_row, pe_column, 'Period To', label_format)

        pe_row += 1
        pe_column = 0
        for pel in lines.project_experiences_lines:
            sheet.write(pe_row, pe_column, pel.name)
            pe_column += 1
            sheet.write(pe_row, pe_column, pel.position)
            pe_column += 1
            sheet.write(pe_row, pe_column, pel.responsibilities)
            pe_column += 1
            sheet.write(pe_row, pe_column, pel.programming_languages)
            pe_column += 1
            sheet.write(pe_row, pe_column, pel.period_from,
                        workbook.add_format({'num_format': 'dd/mm/yyyy'}))
            pe_column += 1
            sheet.write(pe_row, pe_column, pel.period_to,
                        workbook.add_format({'num_format': 'dd/mm/yyyy'}))

            pe_row += 1
            pe_column = 0

        ls_row = pe_row
        ls_column = 0
        sheet.merge_range(ls_row, ls_column, ls_row, ls_column + 5, 'Language Skills', header_format)

        ls_row += 1
        sheet.write(ls_row, ls_column, 'Language', label_format)
        ls_column += 1
        sheet.write(ls_row, ls_column, 'Level', label_format)
        ls_column += 1
        sheet.write(ls_row, ls_column, 'Education Center', label_format)
        ls_column += 1
        sheet.merge_range(ls_row, ls_column, ls_row, ls_column + 2, 'Description', label_format)

        ls_row += 1
        ls_column = 0
        for lsl in lines.language_skills_lines:
            sheet.write(ls_row, ls_column, lsl.name)
            ls_column += 1
            sheet.write(ls_row, ls_column, lsl.level)
            ls_column += 1
            sheet.write(ls_row, ls_column, lsl.education_center)
            ls_column += 1
            sheet.merge_range(ls_row, ls_column, ls_row, ls_column + 2, lsl.description)

            ls_row += 1
            ls_column = 0
