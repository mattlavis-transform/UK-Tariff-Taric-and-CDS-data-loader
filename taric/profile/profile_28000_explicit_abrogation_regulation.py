import common.globals as g


class profile_28000_explicit_abrogation_regulation(object):
    def import_node(self, app, update_type, omsg, transaction_id, message_id, record_code, sub_record_code):
        g.app.message_count += 1
        operation_date = g.app.get_timestamp()
        explicit_abrogation_regulation_role = g.app.get_value(omsg, ".//oub:explicit.abrogation.regulation.role", True)
        explicit_abrogation_regulation_id = g.app.get_value(omsg, ".//oub:explicit.abrogation.regulation.id", True)
        published_date = g.app.get_date_value(omsg, ".//oub:published.date", True)
        officialjournal_number = g.app.get_value(omsg, ".//oub:officialjournal.number", True)
        officialjournal_page = g.app.get_value(omsg, ".//oub:officialjournal.page", True)
        replacement_indicator = g.app.get_value(omsg, ".//oub:replacement.indicator", True)
        abrogation_date = g.app.get_date_value(omsg, ".//oub:abrogation.date", True)
        information_text = g.app.get_value(omsg, ".//oub:information.text", True)
        approved_flag = g.app.get_value(omsg, ".//oub:approved.flag", True)

        # Set operation types and print load message to screen
        operation = g.app.get_loading_message(update_type, "explicit abrogation regulation", explicit_abrogation_regulation_id)

        # Load data
        cur = g.app.conn.cursor()
        try:
            cur.execute("""INSERT INTO explicit_abrogation_regulations_oplog (explicit_abrogation_regulation_role,
            explicit_abrogation_regulation_id, published_date, officialjournal_number,
            officialjournal_page, replacement_indicator, abrogation_date, information_text, approved_flag,
            operation, operation_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (explicit_abrogation_regulation_role,
            explicit_abrogation_regulation_id, published_date, officialjournal_number,
            officialjournal_page, replacement_indicator, abrogation_date, information_text, approved_flag,
            operation, operation_date))
            g.app.conn.commit()
        except:
            g.data_file.record_business_rule_violation("DB", "DB failure", operation, transaction_id, message_id, record_code, sub_record_code, explicit_abrogation_regulation_id)
        cur.close()

        if g.app.perform_taric_validation is True:
            g.app.all_regulations = g.app.get_all_regulations()
