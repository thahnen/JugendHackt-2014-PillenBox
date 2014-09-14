#import <Foundation/Foundation.h>
#import "AFNetworking.h"


@protocol APIClientProtocol <NSObject>

@optional -(void)didFinishRequest:responseObject withAction:action;

@optional -(void)didFinishCheckLogin: responseObject;
@optional -(void)didFinishGetName: responseObject;
@optional -(void)didFinishGetPatientList: responseObject;
@optional -(void)didFinishGetPatientInformation: responseObject;
@optional -(void)didFinishSetPatientInformation: responseObject;

@optional -(void)didFinishGetPillTimeOfPatient: responseObject;
@optional -(void)didFinishGetPillInformationOfPillID: responseObject;
@optional -(void)didFinishSetPillInformationOfPill: responseObject;

@end

@interface APIClient : AFHTTPRequestOperationManager

@property (nonatomic, weak) id <APIClientProtocol> delegate;


-(void)checkLogin;

-(void)sendRequestWithAction: action;
-(void)sendRequestWithAction: action Data: data;

-(void)getPatientList;
-(void)getPatientInformation: patientID;
-(void)setPatientInformation: patientID;

-(void)getPillTimeOfPatient: patientID;
-(void)getPillInformationOfPillID: pillID;
-(void)setPillInformationOfPill: pillID;


@end