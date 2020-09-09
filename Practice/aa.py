bool isOpen()
{
    return m_bConected;
}

bool UpdateCharacter()
{
    if( isOpen() == false )
    {
        if( TryReconnect() == false )
            return false;
    }

    /*
    핸들 할당
    쿼리문 입력
    */

    if( SQLexec( handle, Query ) == OK )
    {
        // 처리 프로세스
    }
    else
    {
        m_bConnected = false;
        return false;
    }
}