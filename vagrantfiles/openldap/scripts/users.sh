#!/bin/bash

BASE_DN="dc=pfernandez,dc=ies"

ADMIN_DN="cn=admin,dc=pfernandez,dc=ies"
ADMIN_PASSWORD="122409"

# FUNCTION TO CREATE USER----------------------------------------------------------------------------------------------------------------
create_user() {
    local OU=$1
    local USERNAME=$2
    local CN=$3
    local SN=$4
    local PASSWORD=$5

    ldapadd -x -H ldap://localhost -D "$ADMIN_DN" -w "$ADMIN_PASSWORD" <<EOF
dn: uid=$USERNAME,ou=$OU,$BASE_DN
objectClass: inetOrgPerson
objectClass: top
cn: $CN
sn: $SN
uid: $USERNAME
userPassword: $PASSWORD
EOF
}

# FUNCTION TO CREATE ADMIN USER----------------------------------------------------------------------------------------------------------
user_admin() {

    ldapadd -x -H ldap://localhost -D "$ADMIN_DN" -w "$ADMIN_PASSWORD" <<EOF
dn: uid=tecAdmin,ou=OU_DPTOTECNICO,dc=pfernandez,dc=ies
objectClass: inetOrgPerson
objectClass: top
cn: admin
sn: admin
uid: tecAdmin
userPassword: 122409
EOF

}

# STUDENTS------------------------------------------------------------------------------------------------------------------------------
for COURSE in OU_PRIMEROESO OU_SEGUNDOESO OU_TERCEROESO OU_PRIMEROBCH OU_SEGUNDOBCH; do
    for i in {1..3}; do
        create_user "$COURSE,ou=OU_ESO" "alumno$i" "Alumno $i" "Curso $COURSE" "122409"
    done
done

for COURSE in OU_DAW OU_DAM OU_SMR OU_ASIR OU_POC OU_PED OU_AF; do
    for i in {1..3}; do
        create_user "$COURSE,ou=OU_FP" "alumno$i" "Alumno $i" "Curso $COURSE" "122409"
    done
done

# TEACHERS ------------------------------------------------------------------------------------------------------------------------------
for DEPT in OU_DPTOINGLES OU_DPTOLENGUA OU_DPTOMATEMATICAS OU_DPTOFOL OU_DPTOGEOGRAFIA OU_DPTOTECNOLOGIA; do
    for i in {1..3}; do
        create_user "$DEPT",ou=OU_PROFESORES "profesor$i" "Profesor $i" "Departamento $DEPT" "122409"
    done
done

for subdept in OU_CIENCIASFISICAS OU_BIOLOGIA; do
    for i in {1..3}; do
        create_user "$subdept,ou=OU_DPTOCIENCIAS",ou=OU_PROFESORES  "profesor$i" "Profesor $i" "Departamento OU_DPTOCIENCIAS" "122409"
    done
done

for subdept in OU_INFORMATICA OU_SISTEMAS; do
    for i in {1..3}; do
        create_user "$subdept,ou=OU_DPTOINFORMATICA",ou=OU_PROFESORES "profesor$i" "Profesor $i" "Departamento OU_DPTOINFORMATICA" "122409"
    done
done    

# ADMIN--------------------------------------------------------------------------------------------------------------------------------
for i in {1..2}; do
    create_user "OU_ADMINISTRACION" "admin$i" "Admin $i" "Administración" "122409"
done

# MANAGEMENT---------------------------------------------------------------------------------------------------------------------------
for i in {1..4}; do
    create_user "OU_EQUIPODIRECTIVO" "directivo$i" "Directivo $i" "Equipo Directivo" "122409"
done

# TECHNIC-----------------------------------------------------------------------------------------------------------------------------

user_admin