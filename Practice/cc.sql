CREATE OR REPLACE FUNCTION sp_delete_item_backuptables(varchar)
RETURNS void AS
$$
BEGIN
	execute 'DROP TABLE ' || 'backup_tb_character_items'          || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_character_cash_items'     || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_character_store'          || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_character_store_extend'   || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_character_deco_items'     || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_consignment_expire_items' || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_consignment_sale_items'   || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_consignment_sell_items'   || '_' || $1 ;
	execute 'DROP TABLE ' || 'backup_tb_post_items'               || '_' || $1 ;
END
$$
LANGUAGE plpgsql;
