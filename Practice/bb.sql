CREATE OR REPLACE FUNCTION sp_move_items_to_backuptables(varchar, integer)
RETURNS void AS
$$
BEGIN
    execute	'INSERT INTO ' || 'backup_tb_character_items'          || '_' || $1 || ' SELECT * FROM tb_character_items WHERE dwid = '                || $2;
    execute 'INSERT INTO ' || 'backup_tb_character_cash_items'     || '_' || $1 || ' SELECT * FROM  tb_character_cash_items WHERE dwid = '          || $2;
    execute 'INSERT INTO ' || 'backup_tb_character_deco_items'     || '_' || $1 || ' SELECT * FROM  tb_character_deco_items WHERE dwid = '          || $2;
    execute 'INSERT INTO ' || 'backup_tb_character_store'          || '_' || $1 || ' SELECT * FROM  tb_character_store WHERE dwid = '               || $2;
    execute 'INSERT INTO ' || 'backup_tb_character_store_extend'   || '_' || $1 || ' SELECT * FROM  tb_character_store_extend WHERE  dwid = '       || $2;
    execute 'INSERT INTO ' || 'backup_tb_post_items'               || '_' || $1 || ' SELECT * FROM  tb_post_items WHERE dwid = '                    || $2;
    execute 'INSERT INTO ' || 'backup_tb_consignment_expire_items' || '_' || $1 || ' SELECT * FROM  tb_consignment_expire_items WHERE  dwitemid = ' || $2;
    execute 'INSERT INTO ' || 'backup_tb_consignment_sale_items'   || '_' || $1 || ' SELECT * FROM  tb_consignment_sale_items WHERE  dwitemid = '   || $2;
    execute 'INSERT INTO ' || 'backup_tb_consignment_sell_items'   || '_' || $1 || ' SELECT * FROM  tb_consignment_sell_items WHERE  dwitemid = '   || $2;

    execute 'DELETE FROM ' || 'tb_character_items'          || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_character_cash_items'     || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_character_store'          || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_character_store_extend'   || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_post_items'               || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_character_deco_items'     || ' WHERE dwid = ' || $2;
    execute 'DELETE FROM ' || 'tb_consignment_expire_items' || ' WHERE dwitemid = ' || $2;
    execute 'DELETE FROM ' || 'tb_consignment_sale_items'   || ' WHERE dwitemid = ' || $2;
    execute 'DELETE FROM ' || 'tb_consignment_sell_items'   || ' WHERE dwitemid = ' || $2;
    execute 'DELETE FROM ' || 'tb_consignment_sale'         || ' WHERE dwauctionid in (SELECT dwauctionid FROM backup_tb_consignment_sale_items_'   || $1 || ' WHERE dwitemid = ' || $2 || ')';
    execute 'DELETE FROM ' || 'tb_consignment_expire'       || ' WHERE dwauctionid in (SELECT dwauctionid FROM backup_tb_consignment_expire_items_' || $1 || ' WHERE dwitemid = ' || $2 || ')';
    execute 'DELETE FROM ' || 'tb_consignment_sell'         || ' WHERE dwauctionid in (SELECT dwauctionid FROM backup_tb_consignment_sell_items_'   || $1 || ' WHERE dwitemid = ' || $2 || ')';

END
$$
LANGUAGE plpgsql;